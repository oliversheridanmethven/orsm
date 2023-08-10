#!/usr/bin/env python3
"""
Tools for parsing images.
"""
import argparse
import logging
import os

from PIL import Image, ImageOps
from common.variables import variable_names_and_objects
from more_itertools import chunked
import numpy as np


class ImageParser:
    """Parses images."""
    supported_file_types = ['.png']
    max_image_length = 10_000
    greyscale_char_map = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\'. '

    def __init__(self, *args, file_path=None, image=None, **kwargs):
        constructor_variables = variable_names_and_objects(file_path, image)
        assert sum([value is not None for variable, value in constructor_variables]) == 1, f"Only one keyword argument can be used to construct the {type(self).__name__}, input were: {constructor_variables}"
        if file_path is not None:
            self.file_path = file_path
            self.file_root, self.file_extension = os.path.splitext(file_path)
            self.file_basename = os.path.basename(self.file_root)
            assert self.file_extension in self.supported_file_types, f"We do not support the file extension: {self.file_extension} "
            self.image = Image.open(self.file_path)
        elif image is not None:
            if isinstance(image, np.ndarray):
                self.image = Image.fromarray(image)
            elif isinstance(image, Image.Image):
                self.image = image
            else:
                raise NotImplementedError(f"We don't know how to construct an {type(self).__name__} with in input image of type: {type(image)}")
        else:
            raise NotImplementedError(f"We don't know how to construct an {type(self).__name__} with the provided inputs.")

    def get_size(self):
        """Returns the size of an image."""
        width, height = self.image.size
        return {"width": width, "height": height}

    @classmethod
    def check_size(cls, *, width, height):
        """Checks valid widths and heights."""
        # TODO: Consider making this a nice decorator?
        for variable, length in variable_names_and_objects(width, height):
            assert isinstance(length, int) and 1 <= length <= cls.max_image_length, f"The length for {variable = } must be strictly positive and up to {cls.max_image_length = }, not {length = }"

    @classmethod
    def new_size(cls, *, width, height, abs_width=None, abs_height=None, scale=None, **kwargs):
        """Determines the new size of an image."""
        cls.check_size(width=width, height=height)
        assert 1 <= sum([kwarg is None for kwarg in [abs_width, abs_height, scale]]) <= 2, f"Inconsistent number of resizing parameters have been specified: {abs_width = }, {abs_height = }, {scale = }"
        if scale is not None:
            assert abs_width is None and abs_height is None, f"{scale = } has been specified alongside absolute resizing parameters."
        if any([kwarg is not None for kwarg in [abs_width, abs_height]]):
            assert scale is None, f"Can't specify a {scale = } factor when absolute resizings have already been specified."

        if scale is not None:
            assert isinstance(scale, (int, float)), f"The {scale = } provided has the wrong type: {type(scale) = }"
            assert 0 < scale <= ImageParser.max_image_length, f"The scaling must be strictly positive and up to {cls.max_image_length}, not {scale = }"
            abs_height = height * scale
            abs_width = width * scale
        else:
            if abs_width is not None and abs_height is not None:
                pass
            else:
                aspect_ratio = width / height
                if abs_width is not None:
                    abs_height = abs_width / aspect_ratio
                else:
                    abs_width = abs_height * aspect_ratio

        abs_height, abs_width = [int(i) for i in [abs_height, abs_width]]
        cls.check_size(width=abs_width, height=abs_height)

        return {"width": abs_width, "height": abs_height}

    def resize(self, *args, **kwargs):
        """Resize the image."""
        original_size = self.get_size()
        new_size = self.new_size(**original_size, **kwargs)
        self.image = self.image.resize(size=(new_size["width"], new_size["height"]))

    @staticmethod
    def add_border(*args, ascii_image, border=None, **kwargs):
        """Adds a border padding to an image."""
        if border is None:
            return ascii_image
        assert isinstance(border, str) and len(border) == 1, f"The {border = } must be a single character string, not: {type(border)}"
        assert border.isprintable() and border.isascii(), f"The border character {border} must be a printable ascii character."
        lines = [f"{border}{line}{border}" for line in ascii_image.split("\n")]
        assert lines, "There are no lines in the image."
        width = len(lines[0])
        hline = border * width
        lines.insert(0, hline)
        lines.append(hline)
        return "\n".join(lines)

    def as_ascii(self, *args, invert=None, threshold_dense_as_blank=None, threshold_sparse_as_blank=None, **kwargs):
        """Tries to turn an image into an ASCII representation."""
        greyscale = ImageOps.grayscale(self.image)
        ascii_character_aspect_ratio_correction = 0.55
        ascii_width, ascii_height = greyscale.size
        ascii_height = int(ascii_height * ascii_character_aspect_ratio_correction)
        greyscale = greyscale.resize(size=(ascii_width, ascii_height))
        pixels = greyscale.getdata()
        colour_map = self.greyscale_char_map
        if threshold_dense_as_blank is not None:
            colour_map = " " * threshold_dense_as_blank + colour_map
        if threshold_sparse_as_blank is not None:
            colour_map = colour_map + " " * threshold_sparse_as_blank
        if invert:
            colour_map = colour_map[::-1]
        new_pixels = greyscale_to_ascii(pixels=pixels, colour_map=colour_map)
        ascii_image = '\n'.join(''.join(line) for line in chunked(new_pixels, self.get_size()["width"]))
        return self.add_border(ascii_image=ascii_image, **kwargs)


def greyscale_to_ascii(*args, pixels, colour_map, **kwargs):
    """
    A multi-stage greyscale to ascii converter.

    This is implemented in several stages to assist in profiling,
    as we found it was a bottle neck in the naive one liner method.
    Instead we have converted much of this to use numpy arrays to
    speed up performance.
    """
    normalisation = (max(pixels) + 1)
    colour_map_scale = len(colour_map)
    pixels = np.array(pixels)
    colour_map = np.array(list(colour_map))
    pixels_colour_indices = pixels * colour_map_scale // normalisation
    ascii_pixels = colour_map[pixels_colour_indices]
    return ''.join(ascii_pixels)


def main(*args, output=None, **kwargs):
    parser = ImageParser(**kwargs)
    parser.resize(**kwargs)
    ascii_image = parser.as_ascii(**kwargs)
    if output:
        with open(output, 'w') as f:
            print(ascii_image, file=f)
    else:
        print(ascii_image)


def add_parser_optional_arguments(*args, parser, **kwargs):
    parser.add_argument("--abs_height", type=int, metavar="HEIGHT", help="The absolute height of the image.")
    parser.add_argument("--abs_width", type=int, metavar="WIDTH", help="The absolute width of the image.")
    parser.add_argument("--scale", type=float, metavar="SCALE", help="The scale of the image.")
    parser.add_argument("--border", type=str, metavar="CHAR", help="What to pad the border with.", default=" ")
    parser.add_argument("--output", type=str, metavar="PATH", help="The path to save the output image.")
    parser.add_argument("--invert", help="Whether to invert the image (useful for differing light or dark terminal themes).", action="store_true")
    parser.add_argument("--threshold_dense_as_blank", type=int, metavar="AMOUNT", help="Whether to threshold the most dense values with blank characters (useful for removing extremely light or dark backgrounds).")
    parser.add_argument("--threshold_sparse_as_blank", type=int, metavar="AMOUNT", help="Whether to threshold the most sparse values with blank characters (useful for removing extremely light or dark backgrounds).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("file_path", type=str, metavar="PATH", help="The path to the image.")
    add_parser_optional_arguments(parser)
    kwargs = vars(parser.parse_args())
    main(**kwargs)

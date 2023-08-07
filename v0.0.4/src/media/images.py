#!/usr/bin/env python3
"""
Tools for parsing images.
"""

import logging
import os
from PIL import Image
from common.variables import variable_names_and_objects
from pandas import notnull

class ImageParser:
    """Parses images."""
    supported_file_types = ['.png']
    max_image_length = 10_000
    def __init__(self, *args, file_path, **kwargs):
        self.file_path = file_path
        self.file_root, self.file_extension = os.path.splitext(file_path)
        self.file_basename = os.path.basename(self.file_root)
        assert self.file_extension in self.supported_file_types, f"We do not support the file extension: {self.file_extension} "
        self.image = Image.open(self.file_path)

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
    def new_size(cls, *, width, height, abs_width=None, abs_height=None, scale=None):
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

    def resize(self, *args, abs_width=None, abs_height=None, scale=None, **kwargs):
        """Resize the image."""
        size = self.get_size()
        new_size = self.new_size(**size)
        self.image = self.image.resize(size=(new_size["height"], new_size["width"]))

    def as_ascii(self, *args, **kwargs):
        """Tries to turn an image into an ASCII representation."""
        pass

if __name__ == "__main__":
    file_name = "/Users/oliver/ClionProjects/testing/data/images/sheridan_methven_original_white_square_circle.png"
    parser = ImageParser(file_path=file_name)
    size = parser.get_size()
    parser.new_size(**size, scale=0.1)
    parser.resize(abs_width=80, abs_height=50)
    ascii_image = parser.as_ascii()
    print(f"The ASCII version of the image is:\n{ascii_image}")


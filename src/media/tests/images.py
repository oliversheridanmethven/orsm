#!/usr/bin/env python3

import unittest
from media.images import ImageParser
from media import images
from common.arguments import all_kwarg_combinations
import sys

import numpy as np
from PIL import Image
from tempfile import TemporaryDirectory
import pathlib
import os
from subprocess import Popen, PIPE
import shlex


class ImageResizing(unittest.TestCase):

    def setUp(self):
        self.size = {"width": 10, "height": 11}  # This ensures some trivial scalings e.g. 0.5 trigger rounding.
        self.parser = ImageParser

    def test_returns_ints(self):
        abs_kwargs_iterator = all_kwarg_combinations(keys=["abs_width", "abs_height"], values=[20, 5, 11, 80])
        scale_kwargs_iterator = all_kwarg_combinations(keys=["scale"], values=[123.123, 0.8765, 0.5])
        for iterator in [abs_kwargs_iterator, scale_kwargs_iterator]:
            for kwargs in iterator:
                if kwargs:
                    for variable, length in self.parser.new_size(**self.size, **kwargs).items():
                        self.assertIsInstance(length, int, f"The {variable = } is not an integer, but instead {length = }")

    def test_scale_1_does_nothing(self):
        self.assertEqual(self.parser.new_size(**self.size, scale=1), self.size)

    def test_scale_invalid(self):
        """
        Scales which:
        zero
        negative
        underflow
        too large
        overflow
        infinity
        nan
        """
        for kwargs in all_kwarg_combinations(keys=["scale"], values=[0, -1, 1e-30, 1e30, sys.float_info.max, float("inf"), float("nan")]):
            if kwargs:
                with self.assertRaises(Exception, msg=f"An exception should have been thrown for {kwargs = }"):
                    size = self.parser.new_size(**self.size, **kwargs)
                    print(f"The size we returned (but shouldn't have) was: {size = }", file=sys.stderr)

    def test_scale(self):
        scale = 3.0
        self.assertEqual(self.parser.new_size(**self.size, scale=scale), {k: scale * v for k, v in self.size.items()})

    def test_absolute_lengths(self):
        desired = {"abs_height": 33, "abs_width": 22}
        self.assertEqual(self.parser.new_size(**self.size, **desired), {k.replace("abs_", ""): v for k, v in desired.items()})

    def test_lengths_invalid(self):
        """
        lengths which:
        zero
        negative
        non_integer
        too large
        nan
        """
        keys = ["width", "height"]
        for kwargs in all_kwarg_combinations(keys=keys, values=[0, -1, 0.3, 1.4, 1e30, float("inf"), float("nan")]):
            if all(key in keys for key in kwargs.keys()):
                with self.assertRaises(Exception, msg=f"The {kwargs = } should fail."):
                    self.parser.check_size(**kwargs)

    def test_bad_scaling_argument_combinations(self):
        for kwargs in all_kwarg_combinations(keys=["abs_width", "abs_height", "scale"], values=[1], min_length=2):
            kwargs = {**self.size, **kwargs}
            if "scale" in kwargs.keys():
                with self.assertRaises(Exception, msg=f"The {kwargs = } combination should fail."):
                    self.parser.new_size(**kwargs)
            else:
                self.parser.new_size(**kwargs)


class ImageCLI(unittest.TestCase):

    def setUp(self):
        example_image_array = np.random.rand(100, 100, 3) * 255
        self.example_image = Image.fromarray(example_image_array.astype('uint8')).convert('RGBA')

    def test_cli(self):
        with TemporaryDirectory() as temp_directory:
            input_path, output_path = [pathlib.Path(f"{os.path.join(temp_directory, file)}") for file in ["example.png", "example.txt"]]
            self.example_image.save(input_path)
            command = shlex.split(f"{sys.executable} {images.__file__} {input_path} --output {output_path}")
            p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            output, err = p.communicate(b"")
            rc = p.returncode
            self.assertEqual(rc, 0, f"We were unable to run the subprocess {command = }, encountering\noutput:\n{output.decode()}\nerror:\n{err.decode()}")
            self.assertTrue(output_path.is_file(), f"We cant find the file: {output_path}")
            self.assertGreater(os.path.getsize(output_path), 0, f"The {output_path = } is expected to be non-empty.")


if __name__ == '__main__':
    unittest.main()

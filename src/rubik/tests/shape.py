#!/usr/bin/env python3
import unittest
from rubik.shapes import shape as Shape
from rubik.colours.default_colours import Colours
from common.variables import variable_names_and_objects


class Printing(unittest.TestCase):

    def test_shape(self):
        """Should print a nicely coloured shape."""
        kwargs = {"N": 3, "M": 4}
        for name, variable in variable_names_and_objects(Shape.Tile,
                                                         Shape.Domino,
                                                         Shape.Strip,
                                                         Shape.Square,
                                                         Shape.Grid,
                                                         Shape.Sheet,
                                                         Shape.Volume,
                                                         Shape.Cube,
                                                         Shape.Triangle,
                                                         Shape.Tetrahedron,
                                                         ):
            print(f"\nTrying to print a {name}")
            shape = variable(**kwargs)
            print(f"{shape!r}")
            print(f"{shape}")
            print(f"{shape = }")


if __name__ == '__main__':
    unittest.main()

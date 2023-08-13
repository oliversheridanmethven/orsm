#!/usr/bin/env python3
import unittest
from rubik.shapes import shape as Shape
from rubik.colours.default_colours import Colours
from common.variables import variable_names_and_objects


class Printing(unittest.TestCase):

    def test_shape(self):
        """Should print a nicely coloured shape."""
        kwargs = {"N": 3, "M": 4}
        args = []
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
            shape = variable(*args, **kwargs)
            print(f"{shape!r}")
            print(f"{shape}")
            print(f"{shape = }")
            print(f"The solved configuration is: {shape.solved_config(*args, **kwargs)}, and should look like {shape.clean_config(*args, **kwargs)}")
            self.assertEqual(shape, shape.clean_config(*args, **kwargs), "Shapes must always start in a clean configuration.")


if __name__ == '__main__':
    unittest.main()

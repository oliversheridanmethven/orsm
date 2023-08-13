#!/usr/bin/env python3
"""
A collection of Rubik style shapes we wish to support.
"""

from rubik.colours.default_colours import Colours
import numpy as np


class Shape:
    """
    A collection of tiles in the form of some shape.
    """

    def __init__(self, *args, root=None, colours=None, **kwargs):
        self.faces = []
        self.colours = colours if colours is not None else Colours

    def __repr__(self):
        return f"{type(self).__name__}(root={self.faces})"

    def __str__(self):
        s = "\n"
        for face in self.faces:
            for tiles in face:
                for tile in tiles:
                    s += f"{self.colours(tile).colour(tile)} "
                s += "\n"
            s += "\n"
        return s

    @classmethod
    def clean_config(cls, *args, **kwargs):
        """What a clean configuration is classified as."""
        return cls(*args, **kwargs)

    @classmethod
    def solved_config(cls, *args, **kwargs):
        """What a solved configuration is classified as."""
        return cls.clean_config(*args, **kwargs).faces

    def __eq__(self, other):
        return self.faces == other.faces


class Tile(Shape):
    """
    A single 1x1x0 square tile.

     ____
    |    |
    |    |
     ----

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for colour in self.colours:
            self.faces.append([[colour.value]])
            if len(self.faces) == 2:
                break
        assert len(self.faces) == 2, f"A {type(self).__name__} must have only 2 faces."
        for face in self.faces:
            assert np.shape(face) == (1, 1), f"A {type(self).__name__} face must only contain 1 tiles"


class Domino(Shape):
    """
    A 2x1x0 set of square tiles.

     ____
    |    |
    |    |
     ----
    |    |
    |    |
     ----

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for colour in self.colours:
            self.faces.append([[colour.value]] * 2)
            if len(self.faces) == 2:
                break
        assert len(self.faces) == 2, f"A {type(self).__name__} must have only 2 faces."
        for face in self.faces:
            assert np.shape(face) == (2, 1), f"A {type(self).__name__} face must only contain 2 tiles."


class Strip(Shape):
    """
    A Nx1x0 set of square tiles with N >=2

     ____
    |    |
    |    |
     ----
    |    |
    |    |
     ----
    |    |
    :    :
    :    :
    :    :
    |    |
     ----
    |    |
    |    |
     ----

    """

    def __init__(self, *args, N, **kwargs):
        super().__init__(*args, **kwargs)
        assert N >= 2, "A strip must be longer than 2."
        for colour in self.colours:
            self.faces.append([[colour.value]] * N)
            if len(self.faces) == 2:
                break
        assert len(self.faces) == 2, f"A {type(self).__name__} must have only 2 faces."
        for face in self.faces:
            assert np.shape(face) == (N, 1), f"A {type(self).__name__} face must only contain 2 tiles."


class Square(Shape):
    """
    A 2x2x0 set of square tiles.

     ____ ____
    |    |    |
    |    |    |
     ---- ----
    |    |    |
    |    |    |
     ---- ----

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for colour in self.colours:
            self.faces.append([[colour.value] * 2] * 2)
            if len(self.faces) == 2:
                break
        assert len(self.faces) == 2, f"A {type(self).__name__} must have only 2 faces."
        for face in self.faces:
            assert np.shape(face) == (2, 2), f"A {type(self).__name__} face must only contain 4 tiles."


class Grid(Shape):
    """
    A NxMx0 set of square tiles with N,M >= 2

     ____ ___...___ ____
    |    |         |    |
    |    |         |    |
     ---- ---...--- ----
    |    |    |    |    |
    :    :    :    :    :
    :    :    :    :    :
    :    :    :    :    :
    |    |    |    |    |
     ---- ---...--- ----
    |    |    |    |    |
    |    |    |    |    |
     ---- ---...--- ----

    """

    def __init__(self, *args, N, M, **kwargs):
        super().__init__(*args, **kwargs)
        for colour in self.colours:
            self.faces.append([[colour.value] * M] * N)
            if len(self.faces) == 2:
                break
        assert len(self.faces) == 2, f"A {type(self).__name__} must have only 2 faces."
        for face in self.faces:
            assert np.shape(face) == (N, M), f"A {type(self).__name__} face must only contain NxM tiles."


class Triangle(Shape):
    """
    A 2x2x0 set of 4 triangular tiles (including the centre piece).

        /\
       /  \
       ----
     /\    /\
    /  \  /  \
    ----  ----
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for colour in self.colours:
            self.faces.append([[colour.value], [colour.value] * 3])
            if len(self.faces) == 2:
                break
        assert len(self.faces) == 2, f"A {type(self).__name__} must have only 2 faces."
        for face in self.faces:
            assert [len(row) for row in face] == [1, 3], f"A {type(self).__name__} face must only contain 16 tiles."


class Tetrahedron(Shape):
    """
    A 2x2x2 set of tetrahedral tiles (including the centre piece).

                 ______
                |  |  /\
                |_/ \/  \
    left --->   | \  ----    <--- right
                |  /\    /\
                | /  \  /  \
                 ----  ----
         _.               ._
         /|               |\
        /                   \
       /                     \
    bottom                  front

    The face ordering is [front, right, left, bottom]
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for colour in self.colours:
            self.faces.append([[colour.value], [colour.value] * 3])
            if len(self.faces) == 4:
                break
        assert len(self.faces) == 4, f"A {type(self).__name__} must have only 4 faces."
        for face in self.faces:
            assert [len(row) for row in face] == [1, 3], f"A {type(self).__name__} face must only contain 16 tiles."


class Sheet(Shape):
    """
    A 2x2x1 set of square tiles.

         top
          |
          |
          V

       ____ ____
     /____/____/|
    |    |    | |
    |    |    |/|
     ---- ----  |   <-- right
    |    |    | |
    |    |    |/
     ---- ----

        _.
        /|
       /
      /
    front

    The faces come in the order
    [front, back, right, left, top, bottom]
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        shapes = [(2, 2), (2, 2), (2, 1), (2, 1), (1, 2), (1, 2)]
        for colour, shape in zip(self.colours, shapes):
            self.faces.append([[colour.value] * shape[1]] * shape[0])
            if len(self.faces) == 6:
                break
        assert len(self.faces) == 6, f"A {type(self).__name__} must have only 6 faces."
        assert [np.shape(face) for face in self.faces] == shapes, f"A {type(self).__name__} face must only contain 16 tiles in the specific shape: {shapes}"


class Volume(Shape):
    """
    A 2x2x2 set of square tiles.

         ____ ____
       /____/____/|
     /____/____/| |
    |    |    | |/|
    |    |    |/| |
     ---- ----  | |
    |    |    | |/
    |    |    |/
     ---- ----

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for colour in self.colours:
            self.faces.append([[colour.value] * 2] * 2)
            if len(self.faces) == 6:
                break
        assert len(self.faces) == 6, f"A {type(self).__name__} must have only 6 faces."
        for face in self.faces:
            assert np.shape(face) == (2, 2), f"A {type(self).__name__} face must only contain 4 tiles."


class Cube(Shape):
    """
    A 3x3x3 set of square tiles. (The classic Rubik's cube).

           ____ ____ ____
         /____/____/____/|
       /____/____/____/| |
     /____/____/____/| |/|
    |    |    |    | |/| |
    |    |    |    |/| | |
     ---- ---- ----  | |/|
    |    |    |    | |/| |
    |    |    |    |/| | |
     ---- ---- ----  | |/
    |    |    |    | |/
    |    |    |    |/
     ---- ---- ----

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for colour in self.colours:
            self.faces.append([[colour.value] * 3] * 3)
            if len(self.faces) == 6:
                break
        assert len(self.faces) == 6, f"A {type(self).__name__} must have only 6 faces."
        for face in self.faces:
            assert np.shape(face) == (3, 3), f"A {type(self).__name__} face must only contain 9 tiles."


if __name__ == "__main__":
    pass

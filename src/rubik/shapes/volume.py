#!/usr/bin/env python3

from .shape import Shape
from common.logger import log
from copy import deepcopy
from rubik.paths.moves import Move
import numpy as np


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

    def __str__(self):
        """Try to show the cube in a very pictorial way."""
        'front 0  back 1  right 2  left 3  top 4  bottom 5'
        top = self.faces[4]
        front = self.faces[0]
        right = self.faces[2]
        left = self.faces[3]
        back = self.faces[1]
        bottom = self.faces[5]
        s = "\n\n"
        indent = 5
        indenting = indent + 3
        for row in top:
            s += ' ' * indenting
            for tile in row:
                s += f"{self.colours(tile).colour(tile)} "
            s += '\n'
            indenting -= 1
        bars = '-' * len(row) * 2
        s += ' ' * indent + '/' + bars + '/'
        for left_row, front_row, right_row, back_row in zip(left, front, right, back):
            s += "\n"
            for tile in left_row:
                s += f"{self.colours(tile).colour(tile)} "
            s += ': '
            for tile in front_row:
                s += f"{self.colours(tile).colour(tile)} "
            s += ': '
            for tile in right_row:
                s += f"{self.colours(tile).colour(tile)} "
            s += ': '
            for tile in back_row:
                s += f"{self.colours(tile).colour(tile)} "
        s += "\n" + ' ' * indent + "\\" + bars + "\\"
        for row in bottom:
            s += '\n'
            indenting += 1
            s += ' ' * indenting
            for tile in row:
                s += f"{self.colours(tile).colour(tile)} "
        s += "\n\n"
        return s

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.faces:
            for colour in self.colours:
                self.faces.append([[colour.value for i in range(2)] for j in range(2)])
                if len(self.faces) == 6:
                    break
        assert len(self.faces) == 6, f"A {type(self).__name__} must have only 6 faces."
        for face in self.faces:
            assert np.shape(face) == (2, 2), f"A {type(self).__name__} face must only contain 4 tiles."

    class move_1(Move):
        """Move the bottom (front -> right)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            faces = deepcopy(shape.faces)
            if not reverse:
                # Moving the row.
                faces[0][1], faces[2][1], faces[1][1], faces[3][1] = faces[3][1], faces[0][1], faces[2][1], faces[1][1]
                # Moving the face.
                faces[5][0][0], faces[5][0][1], faces[5][1][1], faces[5][1][0] = faces[5][1][0], faces[5][0][0], faces[5][0][1], faces[5][1][1]
            else:
                faces[3][1], faces[0][1], faces[2][1], faces[1][1] = faces[0][1], faces[2][1], faces[1][1], faces[3][1]
                faces[5][1][0], faces[5][0][0], faces[5][0][1], faces[5][1][1] = faces[5][0][0], faces[5][0][1], faces[5][1][1], faces[5][1][0]
            assert shape.faces != faces, f"The faces should have changed and should be different."
            return type(self.shape)(*args, faces=faces, **kwargs)

    class move_2(Move):
        """Move the right (front -> top)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            faces = deepcopy(shape.faces)
            if not reverse:
                # Moving the row.
                faces[0][0][1], faces[0][1][1], faces[5][0][1], faces[5][1][1], faces[1][1][0], faces[1][0][0], faces[4][0][1], faces[4][1][1] = \
                    faces[5][0][1], faces[5][1][1], faces[1][1][0], faces[1][0][0], faces[4][0][1], faces[4][1][1], faces[0][0][1], faces[0][1][1],
                # Moving the face.
                faces[2][0][0], faces[2][0][1], faces[2][1][1], faces[2][1][0] = faces[2][1][0], faces[2][0][0], faces[2][0][1], faces[2][1][1]
            else:
                # Moving the row.
                faces[5][0][1], faces[5][1][1], faces[1][1][0], faces[1][0][0], faces[4][0][1], faces[4][1][1], faces[0][0][1], faces[0][1][1] = \
                    faces[0][0][1], faces[0][1][1], faces[5][0][1], faces[5][1][1], faces[1][1][0], faces[1][0][0], faces[4][0][1], faces[4][1][1]
                # Moving the face.
                faces[2][1][0], faces[2][0][0], faces[2][0][1], faces[2][1][1] = faces[2][0][0], faces[2][0][1], faces[2][1][1], faces[2][1][0]

            assert shape.faces != faces, f"The faces should have changed and should be different."
            return type(self.shape)(*args, faces=faces, **kwargs)

    class move_3(Move):
        """Move the back (top -> left)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            faces = deepcopy(shape.faces)
            if not reverse:
                # Moving the row.
                faces[4][0][0], faces[4][0][1], faces[2][0][1], faces[2][1][1], faces[5][1][1], faces[5][1][0], faces[3][1][0], faces[3][0][0] = \
                    faces[2][0][1], faces[2][1][1], faces[5][1][1], faces[5][1][0], faces[3][1][0], faces[3][0][0], faces[4][0][0], faces[4][0][1]
                # Moving the face.
                faces[1][0][0], faces[1][0][1], faces[1][1][1], faces[1][1][0] = faces[1][1][0], faces[1][0][0], faces[1][0][1], faces[1][1][1]
            else:
                # Moving the row.
                faces[2][0][1], faces[2][1][1], faces[5][1][1], faces[5][1][0], faces[3][1][0], faces[3][0][0], faces[4][0][0], faces[4][0][1] = \
                    faces[4][0][0], faces[4][0][1], faces[2][0][1], faces[2][1][1], faces[5][1][1], faces[5][1][0], faces[3][1][0], faces[3][0][0]
                # Moving the face.
                faces[1][1][0], faces[1][0][0], faces[1][0][1], faces[1][1][1] = faces[1][0][0], faces[1][0][1], faces[1][1][1], faces[1][1][0]
            assert shape.faces != faces, f"The faces should have changed and should be different."
            return type(self.shape)(*args, faces=faces, **kwargs)

    _moves = {i: move for i, move in enumerate([move_1, move_2, move_3])}

    @classmethod
    def moves(cls, *args, **kwargs):
        return [move for move in cls._moves]


if __name__ == "__main__":
    pass

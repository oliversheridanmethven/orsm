#!/usr/bin/env python3
from .shape import Shape, _array_from_faces_at_end, _first_update_faces
from common.logger import log
from copy import deepcopy
from rubik.paths.moves import Move
import numpy as np


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
    [front, back, right, left, top, bottom] and the orientation is:

              ----------
             |  top   4 |
     --------------------------------------
    | left 3 | front  0 | right 2 | back 1 |
     --------------------------------------
             | bottom 5 |
              ----------

    where the upper left of each face is the (0,0) entry.
    """

    @_first_update_faces
    def __str__(self):
        """Try to show the cube in a very pictorial way."""
        'front 0  back 1  right 2  left 3  top 4  bottom 5'
        top = self._faces[4]
        front = self._faces[0]
        right = self._faces[2]
        left = self._faces[3]
        back = self._faces[1]
        bottom = self._faces[5]
        s = "\n\n"
        indent = 3
        indenting = indent + 2
        for row in top:
            s += ' ' * indenting
            for tile in row:
                s += f"{self._colours(tile).colour(tile)} "
            s += '\n'
            indenting -= 1
        bars = '-' * len(row) * 2
        s += ' ' * indent + '/' + bars + '/'
        for left_row, front_row, right_row, back_row in zip(left, front, right, back):
            s += "\n"
            for tile in left_row:
                s += f"{self._colours(tile).colour(tile)} "
            s += ': '
            for tile in front_row:
                s += f"{self._colours(tile).colour(tile)} "
            s += ': '
            for tile in right_row:
                s += f"{self._colours(tile).colour(tile)} "
            s += ': '
            for tile in back_row:
                s += f"{self._colours(tile).colour(tile)} "
        s += "\n" + ' ' * indent + "\\" + bars + "\\"
        for row in bottom:
            s += '\n'
            indenting += 1
            s += ' ' * indenting
            for tile in row:
                s += f"{self._colours(tile).colour(tile)} "
        s += "\n\n"
        return s

    @_array_from_faces_at_end
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        shapes = [(2, 2), (2, 2), (2, 1), (2, 1), (1, 2), (1, 2)]
        if len(self._array):
            return
        if not self._faces:
            for colour, shape in zip(self._colours, shapes):
                self._faces.append([[colour.value for i in range(shape[1])] for j in range(shape[0])])
                if len(self._faces) == 6:
                    break
        assert len(self._faces) == 6, f"A {type(self).__name__} must have only 6 faces. {self._faces}"
        assert [np.shape(face) for face in self._faces] == shapes, f"A {type(self).__name__} face must only contain 16 tiles in the specific shape: {shapes}"

    class move_1(Move):
        """Move the bottom."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            array = shape._array
            array = array[[0, 1, 6, 7, 4, 5, 2, 3, 8, 11, 10, 9, 12, 13, 15, 14]]
            return type(shape)(array=array)

    class move_2(Move):
        """Move the right."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            array = shape._array
            array = array[[0, 6, 2, 4, 3, 5, 1, 7, 9, 8, 10, 11, 12, 15, 14, 13]]
            return type(shape)(array=array)

    _moves = {i: move for i, move in enumerate([move_1, move_2])}

    @classmethod
    def moves(cls):
        return [move for move in cls._moves]


if __name__ == "__main__":
    pass

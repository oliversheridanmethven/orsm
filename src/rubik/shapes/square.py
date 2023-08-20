#!/usr/bin/env python3

from .shape import Shape, _array_from_faces_at_end, _first_update_faces
from common.logger import log
from copy import deepcopy
from rubik.paths.moves import Move
import numpy as np


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

    @_array_from_faces_at_end
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if len(self._array):
            return
        if not self._faces:
            for colour in self._colours:
                self._faces.append([[colour.value for j in range(2)] for i in range(2)])
                if len(self._faces) == 2:
                    break
        assert len(self._faces) == 2, f"A {type(self).__name__} must have only 2 faces."
        for face in self._faces:
            assert np.shape(face) == (2, 2), f"A {type(self).__name__} face must only contain 4 tiles."

    @_first_update_faces
    def __str__(self):
        front = self._faces[0]
        back = self._faces[1]
        s = "\n"
        for front_row, back_row in zip(front, back):
            s += "\n"
            for tile in front_row:
                s += f"{self._colours(tile).colour(tile)} "
            s += ': '
            for tile in back_row:
                s += f"{self._colours(tile).colour(tile)} "
        s += "\n\n"
        return s

    class move_1(Move):
        """Move the bottom."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            array = shape._array
            array = array[[0, 1, 6, 7, 4, 5, 2, 3]]
            return type(shape)(array=array)

    class move_2(Move):
        """Move the right."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            array = shape._array
            array = array[[0, 4, 2, 6, 1, 5, 3, 7]]
            return type(shape)(array=array)

    _moves = {i: move for i, move in enumerate([move_1, move_2])}

    _reverse_moves = NotImplemented
    _commutative_moves = NotImplementedError


if __name__ == "__main__":
    pass

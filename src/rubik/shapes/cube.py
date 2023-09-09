#!/usr/bin/env python3

from .shape import Shape, _array_from_faces_at_end
from common.logger import log
from copy import deepcopy
from rubik.paths.move import Move
import numpy as np


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

    @_array_from_faces_at_end
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for colour in self._colours:
            self._faces.append([[colour.value for i in range(3)] for j in range(3)])
            if len(self._faces) == 6:
                break
        assert len(self._faces) == 6, f"A {type(self).__name__} must have only 6 faces."
        for face in self._faces:
            assert np.shape(face) == (3, 3), f"A {type(self).__name__} face must only contain 9 tiles."

    _moves = NotImplementedError
    _reverse_moves = NotImplementedError
    _commutative_moves = NotImplementedError


if __name__ == "__main__":
    pass

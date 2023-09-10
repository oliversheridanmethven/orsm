#!/usr/bin/env python3

from .shape import Shape, _array_from_faces_at_end, _first_update_faces
from .utils import printing_cubic_shapes
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
        if len(self._array):
            return
        if not self._faces:
            for colour in self._colours:
                self._faces.append([[colour.value for i in range(3)] for j in range(3)])
                if len(self._faces) == 6:
                    break
        assert len(self._faces) == 6, f"A {type(self).__name__} must have only 6 faces."
        for face in self._faces:
            assert np.shape(face) == (3, 3), f"A {type(self).__name__} face must only contain 9 tiles."

    @_first_update_faces
    def __str__(self):
        return printing_cubic_shapes.to_string(faces=self._faces, colours=self._colours)

    class move_1(Move):
        """Move the first bottom (front -> right)."""

        # @profile
        def __call__(self, *args, shape, reverse=False, **kwargs):
            array = shape._array
            if not shape._faces:
                shape._update_faces()
            faces = deepcopy(shape._faces)
            if not shape._faces:
                shape._update_faces()
            if not reverse:
                faces[0][2], faces[2][2], faces[1][2], faces[3][2] = faces[3][2], faces[0][2], faces[2][2], faces[1][2]
            else:
                ...
            moved = type(shape)(faces=faces)
            return moved

    class move_2(Move):
        """Move the second bottom (front -> right)."""

        # @profile
        def __call__(self, *args, shape, reverse=False, **kwargs):
            array = shape._array
            if not shape._faces:
                shape._update_faces()
            faces = deepcopy(shape._faces)
            if not shape._faces:
                shape._update_faces()
            if not reverse:
                faces[0][1], faces[2][1], faces[1][1], faces[3][1] = faces[3][1], faces[0][1], faces[2][1], faces[1][1]
            else:
                ...
            moved = type(shape)(faces=faces)
            return moved

    _moves = [move_1, move_2]
    _reverse_moves = NotImplementedError
    _commutative_moves = NotImplementedError


if __name__ == "__main__":
    pass

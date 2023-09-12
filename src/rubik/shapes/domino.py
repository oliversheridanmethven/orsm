#!/usr/bin/env python3

from .shape import Shape, _array_from_faces_at_end
from common.logger import log
from copy import deepcopy
from rubik.paths.move import Move
import numpy as np


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

    @_array_from_faces_at_end
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self._faces:
            for colour in self._colours:
                self._faces.append([[colour.value] for i in range(2)])
                if len(self._faces) == 2:
                    break
        assert len(self._faces) == 2, f"A {type(self).__name__} must have only 2 faces."
        for face in self._faces:
            assert np.shape(face) == (2, 1), f"A {type(self).__name__} face must only contain 2 tiles."

    class move_1(Move):
        """ Move the bottom (front -> back)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            array = shape._array
            # This is the same whether we are in reverse or not...
            array = array[[0, 3, 2, 1]]
            return type(shape)(array=array)

    _moves = [move_1]
    _reverse_moves = {move: reverse_move for move, reverse_move in [(move_1, move_1)]}
    _commutative_moves = ()
    _invariant_tile_positions = ((0, 0, 0), (1, 0, 0))


if __name__ == "__main__":
    pass

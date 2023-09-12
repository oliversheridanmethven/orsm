#!/usr/bin/env python3

import numpy as np
from .shape import Shape, _array_from_faces_at_end


class Tile(Shape):
    """
    A single 1x1x0 square tile.

     ____
    |    |
    |    |
     ----

    """

    @_array_from_faces_at_end
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self._faces:
            for colour in self._colours:
                self._faces.append([[colour.value]])
                if len(self._faces) == 2:
                    break
        assert len(self._faces) == 2, f"A {type(self).__name__} must have only 2 faces."
        for face in self._faces:
            assert np.shape(face) == (1, 1), f"A {type(self).__name__} face must only contain 1 tiles"

    _moves = NotImplemented
    _reverse_moves = NotImplemented
    _commutative_moves = NotImplementedError
    _invariant_tile_positions = NotImplementedError


if __name__ == "__main__":
    pass

#!/usr/bin/env python3

from .shape import Shape, _array_from_faces_at_end
from common.logger import log
from copy import deepcopy
from rubik.paths.moves import Move


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

    @_array_from_faces_at_end
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for colour in self._colours:
            self._faces.append([[colour.value], [colour.value for i in range(3)]])
            if len(self._faces) == 2:
                break
        assert len(self._faces) == 2, f"A {type(self).__name__} must have only 2 faces."
        for face in self._faces:
            assert [len(row) for row in face] == [1, 3], f"A {type(self).__name__} face must only contain 16 tiles."

    _moves = NotImplemented
    _reverse_moves = NotImplemented
    _commutative_moves = NotImplementedError


if __name__ == "__main__":
    pass

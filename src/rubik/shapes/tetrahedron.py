#!/usr/bin/env python3

from .shape import Shape, _array_from_faces_at_end
from common.logger import log
from copy import deepcopy
from rubik.paths.moves import Move


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

    @_array_from_faces_at_end
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for colour in self._colours:
            self._faces.append([[colour.value], [colour.value for i in range(3)]])
            if len(self._faces) == 4:
                break
        assert len(self._faces) == 4, f"A {type(self).__name__} must have only 4 faces."
        for face in self._faces:
            assert [len(row) for row in face] == [1, 3], f"A {type(self).__name__} face must only contain 16 tiles."

    _moves = NotImplemented
    _reverse_moves = NotImplemented
    _commutative_moves = NotImplementedError


if __name__ == "__main__":
    pass

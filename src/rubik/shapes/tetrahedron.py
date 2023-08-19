#!/usr/bin/env python3

from .shape import Shape
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for colour in self.colours:
            self.faces.append([[colour.value], [colour.value for i in range(3)]])
            if len(self.faces) == 4:
                break
        assert len(self.faces) == 4, f"A {type(self).__name__} must have only 4 faces."
        for face in self.faces:
            assert [len(row) for row in face] == [1, 3], f"A {type(self).__name__} face must only contain 16 tiles."

    def moves(self):
        raise NotImplementedError


if __name__ == "__main__":
    pass

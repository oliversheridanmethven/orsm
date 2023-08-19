#!/usr/bin/env python3

from .shape import Shape
from common.logger import log
from copy import deepcopy
from rubik.paths.moves import Move
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.faces:
            for colour in self.colours:
                self.faces.append([[colour.value] for i in range(2)])
                if len(self.faces) == 2:
                    break
        assert len(self.faces) == 2, f"A {type(self).__name__} must have only 2 faces."
        for face in self.faces:
            assert np.shape(face) == (2, 1), f"A {type(self).__name__} face must only contain 2 tiles."

    class move_1(Move):
        def __call__(self, *args, shape, reverse=False, **kwargs):
            faces = deepcopy(shape.faces)
            log.debug(f"The original {shape.faces = }")
            # This is the same whether we are in reverse or not...
            faces[1][1][0], faces[0][1][0] = faces[0][1][0], faces[1][1][0]
            log.debug(f"After swapping {faces = }")
            log.debug(f"The input face after the swapping {shape.faces = }")
            assert shape.faces != faces, f"The faces should have changed and should be different."
            return type(self.shape)(*args, faces=faces, **kwargs)

    def moves(self, *args, **kwargs):

        return [self.move_1(*args, shape=self, **kwargs)]


if __name__ == "__main__":
    pass

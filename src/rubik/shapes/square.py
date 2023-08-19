#!/usr/bin/env python3

from .shape import Shape
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for colour in self.colours:
            self.faces.append([[colour.value for j in range(2)] for i in range(2)])
            if len(self.faces) == 2:
                break
        assert len(self.faces) == 2, f"A {type(self).__name__} must have only 2 faces."
        for face in self.faces:
            assert np.shape(face) == (2, 2), f"A {type(self).__name__} face must only contain 4 tiles."

    def moves(self):
        raise NotImplementedError


if __name__ == "__main__":
    pass

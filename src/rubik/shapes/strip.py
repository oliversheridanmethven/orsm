#!/usr/bin/env python3
from .shape import Shape
from common.logger import log
from copy import deepcopy
from rubik.paths.moves import Move
import numpy as np


class Strip(Shape):
    """
    A Nx1x0 set of square tiles with N >=2

     ____
    |    |
    |    |
     ----
    |    |
    |    |
     ----
    |    |
    :    :
    :    :
    :    :
    |    |
     ----
    |    |
    |    |
     ----

    """

    def __init__(self, *args, N, **kwargs):
        super().__init__(*args, **kwargs)
        assert N >= 2, "A strip must be longer than 2."
        for colour in self.colours:
            self.faces.append([[colour.value] for i in range(N)])
            if len(self.faces) == 2:
                break
        assert len(self.faces) == 2, f"A {type(self).__name__} must have only 2 faces."
        for face in self.faces:
            assert np.shape(face) == (N, 1), f"A {type(self).__name__} face must only contain 2 tiles."

    def moves(self):
        raise NotImplementedError


if __name__ == "__main__":
    pass

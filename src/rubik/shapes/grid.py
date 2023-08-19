#!/usr/bin/env python3

from .shape import Shape
from common.logger import log
from copy import deepcopy
from rubik.paths.moves import Move
import numpy as np


class Grid(Shape):
    """
    A NxMx0 set of square tiles with N,M >= 2

     ____ ___...___ ____
    |    |         |    |
    |    |         |    |
     ---- ---...--- ----
    |    |    |    |    |
    :    :    :    :    :
    :    :    :    :    :
    :    :    :    :    :
    |    |    |    |    |
     ---- ---...--- ----
    |    |    |    |    |
    |    |    |    |    |
     ---- ---...--- ----

    """

    def __init__(self, *args, N, M, **kwargs):
        super().__init__(*args, **kwargs)
        for colour in self._colours:
            self._faces.append([[colour.value for m in range(M)] for n in range(N)])
            if len(self._faces) == 2:
                break
        assert len(self._faces) == 2, f"A {type(self).__name__} must have only 2 faces."
        for face in self._faces:
            assert np.shape(face) == (N, M), f"A {type(self).__name__} face must only contain NxM tiles."

    def moves(self):
        raise NotImplementedError


if __name__ == "__main__":
    pass

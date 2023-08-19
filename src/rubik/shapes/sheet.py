#!/usr/bin/env python3
from .shape import Shape
from common.logger import log
from copy import deepcopy
from rubik.paths.moves import Move
import numpy as np


class Sheet(Shape):
    """
    A 2x2x1 set of square tiles.

         top
          |
          |
          V

       ____ ____
     /____/____/|
    |    |    | |
    |    |    |/|
     ---- ----  |   <-- right
    |    |    | |
    |    |    |/
     ---- ----

        _.
        /|
       /
      /
    front

    The faces come in the order
    [front, back, right, left, top, bottom] and the orientation is:

              ----------
             |  top   4 |
     --------------------------------------
    | left 3 | front  0 | right 2 | back 1 |
     --------------------------------------
             | bottom 5 |
              ----------

    where the upper left of each face is the (0,0) entry.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        shapes = [(2, 2), (2, 2), (2, 1), (2, 1), (1, 2), (1, 2)]
        for colour, shape in zip(self._colours, shapes):
            self._faces.append([[colour.value for i in range(shape[1])] for j in range(shape[0])])
            if len(self._faces) == 6:
                break
        assert len(self._faces) == 6, f"A {type(self).__name__} must have only 6 faces."
        assert [np.shape(face) for face in self._faces] == shapes, f"A {type(self).__name__} face must only contain 16 tiles in the specific shape: {shapes}"

    def moves(self):
        raise NotImplementedError


if __name__ == "__main__":
    pass

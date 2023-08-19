#!/usr/bin/env python3

import numpy as np
from .shape import Shape


class Tile(Shape):
    """
    A single 1x1x0 square tile.

     ____
    |    |
    |    |
     ----

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.faces:
            for colour in self.colours:
                self.faces.append([[colour.value]])
                if len(self.faces) == 2:
                    break
        assert len(self.faces) == 2, f"A {type(self).__name__} must have only 2 faces."
        for face in self.faces:
            assert np.shape(face) == (1, 1), f"A {type(self).__name__} face must only contain 1 tiles"

    def moves(self):
        raise NotImplementedError


if __name__ == "__main__":
    pass

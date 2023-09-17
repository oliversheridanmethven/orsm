#!/usr/bin/env python3
from .shape import Shape, _array_from_faces_at_end, _first_update_faces
from .utils import printing_cubic_shapes
from rubiks.moves.move import Move
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

    @_first_update_faces
    def __str__(self):
        return printing_cubic_shapes.to_string(faces=self._faces, colours=self._colours)

    @_array_from_faces_at_end
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        shapes = [(2, 2), (2, 2), (2, 1), (2, 1), (1, 2), (1, 2)]
        if len(self._array):
            return
        if not self._faces:
            for colour, shape in zip(self._colours, shapes):
                self._faces.append([[colour.value for i in range(shape[1])] for j in range(shape[0])])
                if len(self._faces) == 6:
                    break
        assert len(self._faces) == 6, f"A {type(self).__name__} must have only 6 faces. {self._faces}"
        assert [np.shape(face) for face in self._faces] == shapes, f"A {type(self).__name__} face must only contain 16 tiles in the specific shape: {shapes}"

    class move_1(Move):
        """Move the bottom (front -> back)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            array = shape._array
            array = array[[0, 1, 6, 7, 4, 5, 2, 3, 8, 11, 10, 9, 12, 13, 15, 14]]
            return type(shape)(array=array)

    class move_2(Move):
        """Move the right (front -> back)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            array = shape._array
            array = array[[0, 6, 2, 4, 3, 5, 1, 7, 9, 8, 10, 11, 12, 15, 14, 13]]
            return type(shape)(array=array)

    _moves = [move_1, move_2]
    _reverse_moves = {move: reverse_move for move, reverse_move in [(move_1, move_1), (move_2, move_2)]}
    _commutative_moves = ()
    _invariant_tile_positions = ((0, 0, 0), (4, 0, 0), (3, 0, 0))


if __name__ == "__main__":
    pass

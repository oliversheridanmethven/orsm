#!/usr/bin/env python3

from .shape import Shape, _array_from_faces_at_end, _first_update_faces
from common.logger import log
from copy import deepcopy
from rubik.paths.moves import Move
import numpy as np
from common.profiling import profile


class Volume(Shape):
    """
    A 2x2x2 set of square tiles.

         ____ ____
       /____/____/|
     /____/____/| |
    |    |    | |/|
    |    |    |/| |
     ---- ----  | |
    |    |    | |/
    |    |    |/
     ---- ----

    """

    @_first_update_faces
    def __str__(self):
        """Try to show the cube in a very pictorial way."""
        'front 0  back 1  right 2  left 3  top 4  bottom 5'
        top = self._faces[4]
        front = self._faces[0]
        right = self._faces[2]
        left = self._faces[3]
        back = self._faces[1]
        bottom = self._faces[5]
        s = "\n\n"
        indent = 5
        indenting = indent + 3
        for row in top:
            s += ' ' * indenting
            for tile in row:
                s += f"{self._colours(tile).colour(tile)} "
            s += '\n'
            indenting -= 1
        bars = '-' * len(row) * 2
        s += ' ' * indent + '/' + bars + '/'
        for left_row, front_row, right_row, back_row in zip(left, front, right, back):
            s += "\n"
            for tile in left_row:
                s += f"{self._colours(tile).colour(tile)} "
            s += ': '
            for tile in front_row:
                s += f"{self._colours(tile).colour(tile)} "
            s += ': '
            for tile in right_row:
                s += f"{self._colours(tile).colour(tile)} "
            s += ': '
            for tile in back_row:
                s += f"{self._colours(tile).colour(tile)} "
        s += "\n" + ' ' * indent + "\\" + bars + "\\"
        for row in bottom:
            s += '\n'
            indenting += 1
            s += ' ' * indenting
            for tile in row:
                s += f"{self._colours(tile).colour(tile)} "
        s += "\n\n"
        return s

    @_array_from_faces_at_end
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if len(self._array):
            return
        if not self._faces:
            for colour in self._colours:
                self._faces.append([[colour.value for i in range(2)] for j in range(2)])
                if len(self._faces) == 6:
                    break
        assert len(self._faces) == 6, f"A {type(self).__name__} must have only 6 faces."
        for face in self._faces:
            assert np.shape(face) == (2, 2), f"A {type(self).__name__} face must only contain 4 tiles."

    class move_1(Move):
        """Move the bottom (front -> right)."""

        # @profile
        def __call__(self, *args, shape, reverse=False, **kwargs):
            array = shape._array
            if not reverse:
                array = array[[0, 1, 14, 15, 4, 5, 10, 11, 8, 9, 2, 3, 12, 13, 6, 7, 16, 17, 18, 19, 22, 20, 23, 21]]
            else:
                array = array[[0, 1, 10, 11, 4, 5, 14, 15, 8, 9, 6, 7, 12, 13, 2, 3, 16, 17, 18, 19, 21, 23, 20, 22]]
            return type(shape)(array=array)

    class move_2(Move):
        """Move the bottom (front -> back)."""

        # @profile
        def __call__(self, *args, shape, reverse=False, **kwargs):
            array = shape._array
            array = array[[0, 1, 6, 7, 4, 5, 2, 3, 8, 9, 14, 15, 12, 13, 10, 11, 16, 17, 18, 19, 23, 22, 21, 20]]
            return type(shape)(array=array)

    class move_3(Move):
        """Move the bottom (front -> left)."""

        # @profile
        def __call__(self, *args, shape, reverse=False, **kwargs):
            array = shape._array
            if not reverse:
                array = array[[0, 1, 10, 11, 4, 5, 14, 15, 8, 9, 6, 7, 12, 13, 2, 3, 16, 17, 18, 19, 21, 23, 20, 22]]
            else:
                array = array[[0, 1, 14, 15, 4, 5, 10, 11, 8, 9, 2, 3, 12, 13, 6, 7, 16, 17, 18, 19, 22, 20, 23, 21]]
            return type(shape)(array=array)

    class move_4(Move):
        """Move the right (front -> top)."""

        # @profile
        def __call__(self, *args, shape, reverse=False, **kwargs):
            array = shape._array
            if not reverse:
                array = array[[0, 21, 2, 23, 19, 5, 17, 7, 10, 8, 11, 9, 12, 13, 14, 15, 16, 1, 18, 3, 20, 6, 22, 4]]
            else:
                array = array[[0, 17, 2, 19, 23, 5, 21, 7, 9, 11, 8, 10, 12, 13, 14, 15, 16, 6, 18, 4, 20, 1, 22, 3]]
            return type(shape)(array=array)

    class move_5(Move):
        """Move the right (front -> back)."""

        # @profile
        def __call__(self, *args, shape, reverse=False, **kwargs):
            array = shape._array
            array = array[[0, 6, 2, 4, 3, 5, 1, 7, 11, 10, 9, 8, 12, 13, 14, 15, 16, 21, 18, 23, 20, 17, 22, 19]]
            return type(shape)(array=array)

    class move_6(Move):
        """Move the right (front -> bottom)."""

        # @profile
        def __call__(self, *args, shape, reverse=False, **kwargs):
            array = shape._array
            if not reverse:
                array = array[[0, 17, 2, 19, 23, 5, 21, 7, 9, 11, 8, 10, 12, 13, 14, 15, 16, 6, 18, 4, 20, 1, 22, 3]]
            else:
                array = array[[0, 21, 2, 23, 19, 5, 17, 7, 10, 8, 11, 9, 12, 13, 14, 15, 16, 1, 18, 3, 20, 6, 22, 4]]
            return type(shape)(array=array)

    class move_7(Move):
        """Move the back (top -> left)."""

        # @profile
        def __call__(self, *args, shape, reverse=False, **kwargs):
            array = shape._array
            if not reverse:
                array = array[[0, 1, 2, 3, 6, 4, 7, 5, 8, 23, 10, 22, 17, 13, 16, 15, 9, 11, 18, 19, 20, 21, 12, 14]]
            else:
                array = array[[0, 1, 2, 3, 5, 7, 4, 6, 8, 16, 10, 17, 22, 13, 23, 15, 14, 12, 18, 19, 20, 21, 11, 9]]
            return type(shape)(array=array)

    class move_8(Move):
        """Move the back (top -> bottom)."""

        # @profile
        def __call__(self, *args, shape, reverse=False, **kwargs):
            array = shape._array
            array = array[[0, 1, 2, 3, 7, 6, 5, 4, 8, 14, 10, 12, 11, 13, 9, 15, 23, 22, 18, 19, 20, 21, 17, 16]]
            return type(shape)(array=array)

    class move_9(Move):
        """Move the back (top -> right)."""

        # @profile
        def __call__(self, *args, shape, reverse=False, **kwargs):
            array = shape._array
            if not reverse:
                array = array[[0, 1, 2, 3, 5, 7, 4, 6, 8, 16, 10, 17, 22, 13, 23, 15, 14, 12, 18, 19, 20, 21, 11, 9]]
            else:
                array = array[[0, 1, 2, 3, 6, 4, 7, 5, 8, 23, 10, 22, 17, 13, 16, 15, 9, 11, 18, 19, 20, 21, 12, 14]]
            return type(shape)(array=array)

    _moves = {i: move for i, move in enumerate([move_1, move_2, move_3, move_4, move_5, move_6, move_7, move_8, move_9])}
    _reverse_moves = {move: reverse_move for move, reverse_move in [(move_1, move_3),
                                                                    (move_2, move_2),
                                                                    (move_3, move_1),
                                                                    (move_4, move_6),
                                                                    (move_5, move_5),
                                                                    (move_6, move_4),
                                                                    (move_7, move_9),
                                                                    (move_8, move_8),
                                                                    (move_9, move_7)]}
    _commutative_moves = ((move_1, move_2, move_3), (move_4, move_5, move_6), (move_7, move_8, move_9))


if __name__ == "__main__":
    pass

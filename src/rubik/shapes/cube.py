#!/usr/bin/env python3

from .shape import Shape, _array_from_faces_at_end, _first_update_faces
from .utils import printing_cubic_shapes
from common.logger import log
from copy import deepcopy
from rubik.paths.move import Move
import numpy as np


class Cube(Shape):
    """
    A 3x3x3 set of square tiles. (The classic Rubik's cube).

           ____ ____ ____
         /____/____/____/|
       /____/____/____/| |
     /____/____/____/| |/|
    |    |    |    | |/| |
    |    |    |    |/| | |
     ---- ---- ----  | |/|
    |    |    |    | |/| |
    |    |    |    |/| | |
     ---- ---- ----  | |/
    |    |    |    | |/
    |    |    |    |/
     ---- ---- ----

    """

    @_array_from_faces_at_end
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if len(self._array):
            return
        if not self._faces:
            for colour in self._colours:
                self._faces.append([[colour.value for i in range(3)] for j in range(3)])
                if len(self._faces) == 6:
                    break
        assert len(self._faces) == 6, f"A {type(self).__name__} must have only 6 faces."
        for face in self._faces:
            assert np.shape(face) == (3, 3), f"A {type(self).__name__} face must only contain 9 tiles."

    @_first_update_faces
    def __str__(self):
        return printing_cubic_shapes.to_string(faces=self._faces, colours=self._colours)

    class move__(Move):
        """ TESTING ONLY. """

        # @profile
        def __call__(self, *args, shape, reverse=False, **kwargs):
            array = shape._array
            if not shape._faces:
                shape._update_faces()
            faces = deepcopy(shape._faces)
            if not shape._faces:
                shape._update_faces()
            if not reverse:
                # move the row
                f = faces
                # # moving the back
                f[3][0][0], f[3][1][0], f[3][2][0], \
                    f[5][2][0], f[5][2][1], f[5][2][2], \
                    f[2][2][2], f[2][1][2], f[2][0][2], \
                    f[4][0][2], f[4][0][1], f[4][0][0] \
                    = \
                    f[4][0][2], f[4][0][1], f[4][0][0], \
                        f[3][0][0], f[3][1][0], f[3][2][0], \
                        f[5][2][0], f[5][2][1], f[5][2][2], \
                        f[2][2][2], f[2][1][2], f[2][0][2]

                # # moving the back centre
                # f[3][0][1], f[3][1][1], f[3][2][1], \
                #     f[5][1][0], f[5][1][1], f[5][1][2], \
                #     f[2][2][1], f[2][1][1], f[2][0][1], \
                #     f[4][1][2], f[4][1][1], f[4][1][0] \
                #     = \
                #     f[4][1][2], f[4][1][1], f[4][1][0], \
                #         f[3][0][1], f[3][1][1], f[3][2][1], \
                #         f[5][1][0], f[5][1][1], f[5][1][2], \
                #         f[2][2][1], f[2][1][1], f[2][0][1]

                # moving the right
                # faces[0][0][2], faces[0][1][2], faces[0][2][2], \
                #     faces[5][0][2], faces[5][1][2], faces[5][2][2], \
                #     faces[1][2][0], faces[1][1][0], faces[1][0][0], \
                #     faces[4][0][2], faces[4][1][2], faces[4][2][2] \
                #     = \
                #     faces[5][0][2], faces[5][1][2], faces[5][2][2], \
                #         faces[1][2][0], faces[1][1][0], faces[1][0][0], \
                #         faces[4][0][2], faces[4][1][2], faces[4][2][2], \
                #         faces[0][0][2], faces[0][1][2], faces[0][2][2]

                #  Moving the front.
                # faces[0][2], faces[2][2], faces[1][2], faces[3][2] = faces[3][2], faces[0][2], faces[2][2], faces[1][2]
                # move the face
                faces[1][0][0], faces[1][0][1], faces[1][0][2], faces[1][1][2], faces[1][2][2], faces[1][2][1], faces[1][2][0], faces[1][1][0] = \
                    faces[1][2][0], faces[1][1][0], faces[1][0][0], faces[1][0][1], faces[1][0][2], faces[1][1][2], faces[1][2][2], faces[1][2][1]

                # faces[5][0][0], faces[5][0][1], faces[5][0][2], faces[5][1][2], faces[5][2][2], faces[5][2][1], faces[5][2][0], faces[5][1][0] = \
                #     faces[5][2][0], faces[5][1][0], faces[5][0][0], faces[5][0][1], faces[5][0][2], faces[5][1][2], faces[5][2][2], faces[5][2][1]

                # faces[2][0][0], faces[2][0][1], faces[2][0][2], faces[2][1][2], faces[2][2][2], faces[2][2][1], faces[2][2][0], faces[2][1][0] = \
                #     faces[2][2][0], faces[2][1][0], faces[2][0][0], faces[2][0][1], faces[2][0][2], faces[2][1][2], faces[2][2][2], faces[2][2][1]
            else:
                raise RuntimeError
            moved = type(shape)(faces=faces)
            return moved

    class move_1(Move):
        """Move the second bottom (front -> right)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 2, 30, 31, 32, 6, 7, 8, 9, 10, 11, 21, 22, 23, 15, 16, 17, 18, 19, 20, 3, 4, 5, 24, 25, 26, 27, 28, 29, 12, 13, 14, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]])

    class move_2(Move):
        """Move the second bottom (front -> back)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 2, 12, 13, 14, 6, 7, 8, 9, 10, 11, 3, 4, 5, 15, 16, 17, 18, 19, 20, 30, 31, 32, 24, 25, 26, 27, 28, 29, 21, 22, 23, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]])

    class move_3(Move):
        """Move the second bottom (front -> left)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 2, 21, 22, 23, 6, 7, 8, 9, 10, 11, 30, 31, 32, 15, 16, 17, 18, 19, 20, 12, 13, 14, 24, 25, 26, 27, 28, 29, 3, 4, 5, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]])

    class move_4(Move):
        """Move the first bottom (front -> right)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 2, 3, 4, 5, 33, 34, 35, 9, 10, 11, 12, 13, 14, 24, 25, 26, 18, 19, 20, 21, 22, 23, 6, 7, 8, 27, 28, 29, 30, 31, 32, 15, 16, 17, 36, 37, 38, 39, 40, 41, 42, 43, 44, 51, 48, 45, 52, 49, 46, 53, 50, 47]])

    class move_5(Move):
        """Move the first bottom (front -> back)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 2, 3, 4, 5, 15, 16, 17, 9, 10, 11, 12, 13, 14, 6, 7, 8, 18, 19, 20, 21, 22, 23, 33, 34, 35, 27, 28, 29, 30, 31, 32, 24, 25, 26, 36, 37, 38, 39, 40, 41, 42, 43, 44, 53, 52, 51, 50, 49, 48, 47, 46, 45]])

    class move_6(Move):
        """Move the first bottom (front -> left)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 2, 3, 4, 5, 24, 25, 26, 9, 10, 11, 12, 13, 14, 33, 34, 35, 18, 19, 20, 21, 22, 23, 15, 16, 17, 27, 28, 29, 30, 31, 32, 6, 7, 8, 36, 37, 38, 39, 40, 41, 42, 43, 44, 47, 50, 53, 46, 49, 52, 45, 48, 51]])

    class move_7(Move):
        """Move all the bottom (front -> right)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 2, 30, 31, 32, 33, 34, 35, 9, 10, 11, 21, 22, 23, 24, 25, 26, 18, 19, 20, 3, 4, 5, 6, 7, 8, 27, 28, 29, 12, 13, 14, 15, 16, 17, 36, 37, 38, 39, 40, 41, 42, 43, 44, 51, 48, 45, 52, 49, 46, 53, 50, 47]])

    class move_8(Move):
        """Move all the bottom (front -> back)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 2, 12, 13, 14, 15, 16, 17, 9, 10, 11, 3, 4, 5, 6, 7, 8, 18, 19, 20, 30, 31, 32, 33, 34, 35, 27, 28, 29, 21, 22, 23, 24, 25, 26, 36, 37, 38, 39, 40, 41, 42, 43, 44, 53, 52, 51, 50, 49, 48, 47, 46, 45]])

    class move_9(Move):
        """Move all the bottom (front -> left)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 2, 21, 22, 23, 24, 25, 26, 9, 10, 11, 30, 31, 32, 33, 34, 35, 18, 19, 20, 12, 13, 14, 15, 16, 17, 27, 28, 29, 3, 4, 5, 6, 7, 8, 36, 37, 38, 39, 40, 41, 42, 43, 44, 47, 50, 53, 46, 49, 52, 45, 48, 51]])

    class move_10(Move):
        """Move the second right (front -> top)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 46, 2, 3, 49, 5, 6, 52, 8, 9, 43, 11, 12, 40, 14, 15, 37, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 1, 38, 39, 4, 41, 42, 7, 44, 45, 16, 47, 48, 13, 50, 51, 10, 53]])

    class move_11(Move):
        """Move the second right (front -> back)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 16, 2, 3, 13, 5, 6, 10, 8, 9, 7, 11, 12, 4, 14, 15, 1, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 46, 38, 39, 49, 41, 42, 52, 44, 45, 37, 47, 48, 40, 50, 51, 43, 53]])

    class move_12(Move):
        """Move the second right (front -> bottom)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 37, 2, 3, 40, 5, 6, 43, 8, 9, 52, 11, 12, 49, 14, 15, 46, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 16, 38, 39, 13, 41, 42, 10, 44, 45, 1, 47, 48, 4, 50, 51, 7, 53]])

    class move_13(Move):
        """Move the first right (front -> top)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 47, 3, 4, 50, 6, 7, 53, 44, 10, 11, 41, 13, 14, 38, 16, 17, 24, 21, 18, 25, 22, 19, 26, 23, 20, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 2, 39, 40, 5, 42, 43, 8, 45, 46, 15, 48, 49, 12, 51, 52, 9]])

    class move_14(Move):
        """Move the first right (front -> back)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 15, 3, 4, 12, 6, 7, 9, 8, 10, 11, 5, 13, 14, 2, 16, 17, 26, 25, 24, 23, 22, 21, 20, 19, 18, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 47, 39, 40, 50, 42, 43, 53, 45, 46, 38, 48, 49, 41, 51, 52, 44]])

    class move_15(Move):
        """Move the first right (front -> bottom)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 38, 3, 4, 41, 6, 7, 44, 53, 10, 11, 50, 13, 14, 47, 16, 17, 20, 23, 26, 19, 22, 25, 18, 21, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 15, 39, 40, 12, 42, 43, 9, 45, 46, 2, 48, 49, 5, 51, 52, 8]])

    class move_16(Move):
        """Move all the right (front -> top)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 46, 47, 3, 49, 50, 6, 52, 53, 44, 43, 11, 41, 40, 14, 38, 37, 17, 24, 21, 18, 25, 22, 19, 26, 23, 20, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 1, 2, 39, 4, 5, 42, 7, 8, 45, 16, 15, 48, 13, 12, 51, 10, 9]])

    class move_17(Move):
        """Move all the right (front -> back)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 16, 15, 3, 13, 12, 6, 10, 9, 8, 7, 11, 5, 4, 14, 2, 1, 17, 26, 25, 24, 23, 22, 21, 20, 19, 18, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 46, 47, 39, 49, 50, 42, 52, 53, 45, 37, 38, 48, 40, 41, 51, 43, 44]])

    class move_18(Move):
        """Move all the right (front -> bottom)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 37, 38, 3, 40, 41, 6, 43, 44, 53, 52, 11, 50, 49, 14, 47, 46, 17, 20, 23, 26, 19, 22, 25, 18, 21, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 16, 15, 39, 13, 12, 42, 10, 9, 45, 1, 2, 48, 4, 5, 51, 7, 8]])

    class move_19(Move):
        """Move the second back (top -> left)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 50, 20, 21, 49, 23, 24, 48, 26, 27, 41, 29, 30, 40, 32, 33, 39, 35, 36, 37, 38, 19, 22, 25, 42, 43, 44, 45, 46, 47, 28, 31, 34, 51, 52, 53]])

    class move_20(Move):
        """Move the second back (top -> bottom)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 34, 20, 21, 31, 23, 24, 28, 26, 27, 25, 29, 30, 22, 32, 33, 19, 35, 36, 37, 38, 50, 49, 48, 42, 43, 44, 45, 46, 47, 41, 40, 39, 51, 52, 53]])

    class move_21(Move):
        """Move the second back (top -> right)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 39, 20, 21, 40, 23, 24, 41, 26, 27, 48, 29, 30, 49, 32, 33, 50, 35, 36, 37, 38, 34, 31, 28, 42, 43, 44, 45, 46, 47, 25, 22, 19, 51, 52, 53]])

    class move_22(Move):
        """Move the first back (top -> left)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 12, 9, 16, 13, 10, 17, 14, 11, 18, 19, 53, 21, 22, 52, 24, 25, 51, 38, 28, 29, 37, 31, 32, 36, 34, 35, 20, 23, 26, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 27, 30, 33]])

    class move_23(Move):
        """Move the first back (top -> bottom)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 2, 3, 4, 5, 6, 7, 8, 17, 16, 15, 14, 13, 12, 11, 10, 9, 18, 19, 33, 21, 22, 30, 24, 25, 27, 26, 28, 29, 23, 31, 32, 20, 34, 35, 53, 52, 51, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 38, 37, 36]])

    class move_24(Move):
        """Move the first back (top -> right)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 14, 17, 10, 13, 16, 9, 12, 15, 18, 19, 36, 21, 22, 37, 24, 25, 38, 51, 28, 29, 52, 31, 32, 53, 34, 35, 33, 30, 27, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 26, 23, 20]])

    class move_25(Move):
        """Move all the back (top -> left)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 12, 9, 16, 13, 10, 17, 14, 11, 18, 50, 53, 21, 49, 52, 24, 48, 51, 38, 41, 29, 37, 40, 32, 36, 39, 35, 20, 23, 26, 19, 22, 25, 42, 43, 44, 45, 46, 47, 28, 31, 34, 27, 30, 33]])

    class move_26(Move):
        """Move all the back (top -> bottom)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 2, 3, 4, 5, 6, 7, 8, 17, 16, 15, 14, 13, 12, 11, 10, 9, 18, 34, 33, 21, 31, 30, 24, 28, 27, 26, 25, 29, 23, 22, 32, 20, 19, 35, 53, 52, 51, 50, 49, 48, 42, 43, 44, 45, 46, 47, 41, 40, 39, 38, 37, 36]])

    class move_27(Move):
        """Move all the back (top -> right)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 14, 17, 10, 13, 16, 9, 12, 15, 18, 39, 36, 21, 40, 37, 24, 41, 38, 51, 48, 29, 52, 49, 32, 53, 50, 35, 33, 30, 27, 34, 31, 28, 42, 43, 44, 45, 46, 47, 25, 22, 19, 26, 23, 20]])

    class move_x(Move):
        """Move XXX (YYY -> ZZZ)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            return type(shape)(array=shape._array[[]])

    _moves = [move_1, move_2, move_3, move_4, move_5, move_6, move_7, move_8, move_9,
              move_10, move_11, move_12, move_13, move_14, move_15, move_16, move_17, move_18,
              move_19, move_20, move_21, move_22, move_23, move_24, move_25, move_26, move_27]
    # _moves = [move__]
    # _moves = []
    # _moves = [move_4, move_25]
    _reverse_moves = NotImplementedError
    _commutative_moves = NotImplementedError


if __name__ == "__main__":
    pass

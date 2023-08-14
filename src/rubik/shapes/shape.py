#!/usr/bin/env python3
"""
A collection of Rubik style shapes we wish to support.
"""

from common.logger import log
from rubik.colours.default_colours import Colours
import numpy as np
from abc import ABC, abstractmethod
from copy import deepcopy


class Move(ABC):

    def __init__(self, *args, shape, **kwargs):
        self.shape = shape

    @abstractmethod
    def __call__(self, *args, shape, reverse=False, **kwargs):
        # TODO: For better (best?) performance, I will want to permute the tiles using a single numpy array permutation.
        raise NotImplementedError

    def __eq__(self, other):
        # NB, the move definitions can't be in a <locals> namespace
        # for the types to compare equal, hence when defined they should
        # done so outside of any local scope.
        return isinstance(other, type(self)) and other.shape == self.shape


class Shape(ABC):
    """
    A collection of tiles in the form of some shape.
    """

    def __init__(self, *args, faces=None, colours=None, **kwargs):
        self.faces = [] if faces is None else faces
        # TODO: Rather than a list of lists, make the faces a single contiguous numpy array and then
        # add some other data type which says how this is nicely partitioned for printing.
        self.colours = Colours if colours is None else colours

    def __repr__(self):
        obj = f"{type(self).__name__}(faces={self.faces})"
        log.debug(f"The {obj = }{self}")
        return obj

    def __str__(self):
        s = "\n"
        for face in self.faces:
            for tiles in face:
                for tile in tiles:
                    s += f"{self.colours(tile).colour(tile)} "
                s += "\n"
            s += "\n"
        return s

    def __eq__(self, other):
        return self.faces == other.faces

    @classmethod
    def clean_config(cls, *args, **kwargs):
        """What a clean configuration is classified as."""
        return cls(*args, **kwargs)

    @classmethod
    def solved_config(cls, *args, **kwargs):
        """What a solved configuration is classified as."""
        return cls.clean_config(*args, **kwargs)

    def move(self, *moves, **kwargs):
        assert moves, f"There are no moves specified for {self.__name__}"
        moved = self
        for move in moves:
            assert isinstance(move, Move)
            moved = move(shape=moved, **kwargs)
        return moved

    @abstractmethod
    def moves(self, **kwargs):
        ...


class A(ABC):
    pass


class B(A):
    pass


b = B()
isinstance(b, A)


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

    def moves(self, *args, **kwargs):
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

        return [move_1(*args, shape=self, **kwargs)]


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
        for colour in self.colours:
            self.faces.append([[colour.value for m in range(M)] for n in range(N)])
            if len(self.faces) == 2:
                break
        assert len(self.faces) == 2, f"A {type(self).__name__} must have only 2 faces."
        for face in self.faces:
            assert np.shape(face) == (N, M), f"A {type(self).__name__} face must only contain NxM tiles."

    def moves(self):
        raise NotImplementedError


class Triangle(Shape):
    """
    A 2x2x0 set of 4 triangular tiles (including the centre piece).

        /\
       /  \
       ----
     /\    /\
    /  \  /  \
    ----  ----
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for colour in self.colours:
            self.faces.append([[colour.value], [colour.value for i in range(3)]])
            if len(self.faces) == 2:
                break
        assert len(self.faces) == 2, f"A {type(self).__name__} must have only 2 faces."
        for face in self.faces:
            assert [len(row) for row in face] == [1, 3], f"A {type(self).__name__} face must only contain 16 tiles."

    def moves(self):
        raise NotImplementedError


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
        for colour, shape in zip(self.colours, shapes):
            self.faces.append([[colour.value for i in range(shape[1])] for j in range(shape[0])])
            if len(self.faces) == 6:
                break
        assert len(self.faces) == 6, f"A {type(self).__name__} must have only 6 faces."
        assert [np.shape(face) for face in self.faces] == shapes, f"A {type(self).__name__} face must only contain 16 tiles in the specific shape: {shapes}"

    def moves(self):
        raise NotImplementedError


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.faces:
            for colour in self.colours:
                self.faces.append([[colour.value for i in range(2)] for j in range(2)])
                if len(self.faces) == 6:
                    break
        assert len(self.faces) == 6, f"A {type(self).__name__} must have only 6 faces."
        for face in self.faces:
            assert np.shape(face) == (2, 2), f"A {type(self).__name__} face must only contain 4 tiles."

    class move_1(Move):
        """Move the bottom (front -> right)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            faces = deepcopy(shape.faces)
            if not reverse:
                # Moving the row.
                faces[0][1], faces[2][1], faces[1][1], faces[3][1] = faces[3][1], faces[0][1], faces[2][1], faces[1][1]
                # Moving the face.
                faces[5][0][0], faces[5][0][1], faces[5][1][1], faces[5][1][0] = faces[5][1][0], faces[5][0][0], faces[5][0][1], faces[5][1][1]
            else:
                faces[3][1], faces[0][1], faces[2][1], faces[1][1] = faces[0][1], faces[2][1], faces[1][1], faces[3][1]
                faces[5][1][0], faces[5][0][0], faces[5][0][1], faces[5][1][1] = faces[5][0][0], faces[5][0][1], faces[5][1][1], faces[5][1][0]
            assert shape.faces != faces, f"The faces should have changed and should be different."
            return type(self.shape)(*args, faces=faces, **kwargs)

    class move_2(Move):
        """Move the right (front -> top)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            faces = deepcopy(shape.faces)
            if not reverse:
                # Moving the row.
                tmp = faces[0][0][1]  # This will go in [4][1][1]
                faces[0][0][1] = faces[0][1][1]
                faces[0][1][1] = faces[5][0][1]
                faces[5][0][1] = faces[5][1][1]
                faces[5][1][1] = faces[1][1][0]
                faces[1][1][0] = faces[1][0][0]
                faces[1][0][0] = faces[4][0][1]
                faces[4][0][1] = faces[4][1][1]
                faces[4][1][1] = tmp
                # Moving the face.
                faces[2][0][0], faces[2][0][1], faces[2][1][1], faces[2][1][0] = faces[2][1][0], faces[2][0][0], faces[2][0][1], faces[2][1][1]
            else:
                tmp = faces[4][1][1]
                faces[4][1][1] = faces[4][0][1]
                faces[4][0][1] = faces[1][0][0]
                faces[1][0][0] = faces[1][1][0]
                faces[1][1][0] = faces[5][1][1]
                faces[5][1][1] = faces[5][0][1]
                faces[5][0][1] = faces[0][1][1]
                faces[0][1][1] = faces[0][0][1]
                faces[0][0][1] = tmp
                # Moving the face.
                faces[2][1][0], faces[2][0][0], faces[2][0][1], faces[2][1][1] = faces[2][0][0], faces[2][0][1], faces[2][1][1], faces[2][1][0]

            assert shape.faces != faces, f"The faces should have changed and should be different."
            return type(self.shape)(*args, faces=faces, **kwargs)

    class move_3(Move):
        """Move the back (top -> left)."""

        def __call__(self, *args, shape, reverse=False, **kwargs):
            faces = deepcopy(shape.faces)
            if not reverse:
                # Moving the row.
                tmp = faces[4][0][0]
                faces[4][0][0] = faces[4][0][1]
                faces[4][0][1] = faces[2][0][1]
                faces[2][0][1] = faces[2][1][1]
                faces[2][1][1] = faces[5][1][1]
                faces[5][1][1] = faces[5][1][0]
                faces[5][1][0] = faces[3][1][0]
                faces[3][1][0] = faces[3][0][0]
                faces[3][0][0] = tmp
                # Moving the face.
                faces[1][0][0], faces[1][0][1], faces[1][1][1], faces[1][1][0] = faces[1][1][0], faces[1][0][0], faces[1][0][1], faces[1][1][1]
            else:
                # Moving the row.
                tmp = faces[3][0][0]
                faces[3][0][0] = faces[3][1][0]
                faces[3][1][0] = faces[5][1][0]
                faces[5][1][0] = faces[5][1][1]
                faces[5][1][1] = faces[2][1][1]
                faces[2][1][1] = faces[2][0][1]
                faces[2][0][1] = faces[4][0][1]
                faces[4][0][1] = faces[4][0][0]
                faces[4][0][0] = tmp
                # Moving the face.
                faces[1][1][0], faces[1][0][0], faces[1][0][1], faces[1][1][1] = faces[1][0][0], faces[1][0][1], faces[1][1][1], faces[1][1][0]
            assert shape.faces != faces, f"The faces should have changed and should be different."
            return type(self.shape)(*args, faces=faces, **kwargs)

    def moves(self, *args, **kwargs):
        return [move(*args, shape=self, **kwargs) for move in [self.move_1, self.move_2, self.move_3]]


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for colour in self.colours:
            self.faces.append([[colour.value for i in range(3)] for j in range(3)])
            if len(self.faces) == 6:
                break
        assert len(self.faces) == 6, f"A {type(self).__name__} must have only 6 faces."
        for face in self.faces:
            assert np.shape(face) == (3, 3), f"A {type(self).__name__} face must only contain 9 tiles."

    def moves(self):
        raise NotImplementedError


if __name__ == "__main__":
    pass

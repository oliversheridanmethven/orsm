#!/usr/bin/env python3
"""
A collection of Rubik style shapes we wish to support.
"""

from common.logger import log
from rubik.colours.colour_palette import ColourPalette
import numpy as np
from abc import ABC, abstractmethod
import itertools
import random
from rubik.paths.path import Path
from rubik.paths.move import Move
from functools import wraps
from copy import deepcopy


def _array_from_faces_at_end(func):
    """Set the underlying array from an initialisation using faces."""

    @wraps(func)
    def _array_from_faces_at_end_wrapper(self, *args, **kwargs):
        res = func(self, *args, **kwargs)
        if not len(self._array):
            self._update_array()
        return res

    return _array_from_faces_at_end_wrapper


def _first_update_faces(func):
    """We ensure the faces are up to date before calling the function."""

    @wraps(func)
    def _first_update_faces_wrapper(self, *args, **kwargs):
        self._update_faces()
        return func(self, *args, **kwargs)

    return _first_update_faces_wrapper


class Shape(ABC):
    """
    A collection of tiles in the form of some shape.
    """

    def _update_array(self):
        self._array = self.to_array()

    def _update_faces(self):
        new = self.clean_config(*self._args, **self._kwargs)
        # The above ensures we have the correct set of nested lists.
        values = (i for i in self._array)
        new.assign_tiles(values=values)
        self._faces = new._faces

    # @_array_from_faces_at_end
    def __init__(self, *args, array=None, faces=None, colours=None, **kwargs):
        self._array = np.array([]) if array is None else array
        # The _array is our underlying invariant which will always be in a correct state.
        self._colours = ColourPalette if colours is None else colours
        self._faces = [] if faces is None else faces
        self._args = args
        self._kwargs = kwargs

    def __repr__(self):
        # NB ^ Do not wrap this! (The debugger calls the repr at each breakpoint), so wrappers can't have side effects.
        # because we can't wrap it, we do a poor man's wrapping of @_first_update_faces acting on a new object instead.
        # This is definitely a code smell...
        new = type(self)(*self._args, array=self._array, **self._kwargs)
        obj = f"{type(self).__name__}(array={new._array})"
        return obj

    @_first_update_faces
    def __str__(self):
        s = "\n"
        for face in self._faces:
            for tiles in face:
                for tile in tiles:
                    s += f"{self._colours(tile).colour(tile)} "
                s += "\n"
            s += "\n"
        return s

    def __eq__(self, other):
        return all(self._array == other._array)

    def __hash__(self):
        return hash(self.__repr__())

    @classmethod
    def clean_config(cls, *args, **kwargs):
        """What a clean configuration is classified as."""
        return cls(*args, **kwargs)

    @classmethod
    def solved_config(cls, *args, **kwargs):
        """What a solved configuration is classified as."""
        return cls.clean_config(*args, **kwargs)

    def traverse_tiles(self, *args, function, **kwargs):
        for face in self._faces:
            for row in face:
                for tile in row:
                    yield function(tile)

    def assign_tiles(self, *args, values, **kwargs):
        get_values = (i for i in values)
        tmp_faces = deepcopy(self._faces)
        for f, face in enumerate(tmp_faces):
            for r, row in enumerate(face):
                for t, tile in enumerate(row):
                    tmp_faces[f][r][t] = next(get_values)
        self._faces = None
        assert self._faces is None
        self._faces = tmp_faces
        pass

    def to_array(self, *args, **kwargs):
        def return_tile_value(tile):
            return tile

        return np.array(list(self.traverse_tiles(function=return_tile_value)))

    @classmethod
    def from_array(cls, *args, array, **kwargs):
        array_values = (i for i in array)
        new = cls()
        new.assign_tiles(values=array_values)
        return new

    def move(self, *moves, copy_faces=False, reverse=False, **kwargs):
        if not moves:
            log.info(f"There are no moves specified for {type(self).__name__}")
        moved = type(self)(array=self._array, **kwargs)
        if copy_faces:
            # This is helpful in tests and debugging where we might want to perform a move
            # on a shape where the face values aren't colours. Examples would be where the face
            # values are indices, in which case this makes finding the lists of permutation indices
            # easier to find.
            moved._faces = deepcopy(self._faces)
        for move in moves:
            assert isinstance(move, (Move, int)), f"{move = } is of the wrong type: {type(move) = }"
            if isinstance(move, int):
                move = self._moves[move](shape=self)
            reverse_all_moves = reverse
            if reverse:
                move = self.reverse_of(move)
                reverse_all_moves = False
            moved = move(shape=moved, reverse=reverse_all_moves, **kwargs)

        return moved

    @abstractmethod
    def _moves(self):
        """A container to hold the moves."""
        ...

    @abstractmethod
    def _reverse_moves(self):
        """A container to hold the mappings between the moves and the reverse moves."""
        ...

    @abstractmethod
    def _commutative_moves(self):
        """A container to hold the mappings between the moves which commute."""
        ...

    @classmethod
    def moves(cls, *args, **kwargs):
        # Working with moves as indices can make the path constructions generally much quicker.
        # But not as nice for printing though...
        return [move(*args, shape=cls(), **kwargs) for move in cls._moves]
        # return cls._moves

    @classmethod
    def _reverse_moves_mapping(cls, *args, **kwargs):
        return {move(*args, shape=cls(), **kwargs): reverse_move(*args, shape=cls(), **kwargs) for move, reverse_move in cls._reverse_moves.items()}

    @classmethod
    def reverse_of(cls, move, **kwargs):
        moves_mapping = cls._reverse_moves_mapping()
        reverse_move = moves_mapping[move]
        assert isinstance(reverse_move, Move), f"We are returning the wrong type."
        return reverse_move

    @classmethod
    def commutative(cls, move_1, move_2, *args, **kwargs):
        commutative_moves = [[move(*args, shape=cls(), **kwargs) for move in moves] for moves in cls._commutative_moves]
        results = [move_2 in moves for moves in commutative_moves if move_1 in moves]
        assert len(results) >= 1
        return any(results)

    def shuffle(self, *args, turns=100, seed=False, **kwargs):
        """Produces a shuffled cube, and lists how it got there."""
        assert isinstance(turns, int) and turns >= 0, f"Invalid amount of {turns = } specified."
        path = Path(self)
        shuffled = type(self)(faces=self._faces, **kwargs)
        if turns == 0:
            return shuffled, path
        if seed or (isinstance(seed, int) and type(seed) != bool):
            log.debug(f"Seeding the random number with {seed = }")
            assert isinstance(seed, int) and seed >= 0, f"Invalid {seed = }"
            random.seed(seed)
        else:
            random.seed(None)

        last_move = None
        for turn in range(turns):
            # We try and generate a new move (which is not the reverse of the preceding!).
            while True:
                move = random.choices(self.moves())[0]
                if last_move is not None and self.commutative(move, last_move):
                    continue

                last_move = move
                break

            log.debug(f"{turn = } shuffling with {move = }")
            shuffled = shuffled.move(move)
            path._append(move=move, reverse=False)

        return shuffled, path


if __name__ == "__main__":
    pass

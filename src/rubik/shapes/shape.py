#!/usr/bin/env python3
"""
A collection of Rubik style shapes we wish to support.
"""

from common.logger import log
from rubik.colours.default_colours import Colours
import numpy as np
from abc import ABC, abstractmethod
import itertools
import random
from rubik.paths.paths import Path
from rubik.paths.moves import Move
from functools import wraps


def _array_from_faces(func):
    """Set the underlying array from an initialisation using faces."""

    @wraps(func)
    def _array_from_faces_at_end(self, *args, **kwargs):
        func(self, *args, **kwargs)
        log.debug(f"Updating the array from the faces definition")
        if not len(self._array):
            self._update_array()

    return _array_from_faces_at_end


class Shape(ABC):
    """
    A collection of tiles in the form of some shape.
    """

    def _update_array(self):
        self._array = self.to_array()

    # @_array_from_faces
    def __init__(self, *args, array=None, faces=None, colours=None, **kwargs):
        self._faces = [] if faces is None else faces
        # TODO: Rather than a list of lists, make the faces a single contiguous numpy array and then
        # add some other data type which says how this is nicely partitioned for printing.
        self._colours = Colours if colours is None else colours
        self._array = np.array([]) if array is None else array

    def __repr__(self):
        obj = f"{type(self).__name__}(faces={self._faces})"
        return obj

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
        for face in self._faces:
            for row in face:
                for i in range(len(row)):
                    row[i] = next(get_values)

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

    def move(self, *moves, **kwargs):
        if not moves:
            log.info(f"There are no moves specified for {type(self).__name__}")
        moved = type(self)(array=self._array, **kwargs)
        for move in moves:
            assert isinstance(move, (Move, int)), f"{move = } is of the wrong type: {type(move) = }"
            if isinstance(move, int):
                move = self._moves[move](shape=self)
            moved = move(shape=moved, **kwargs)

        return moved

    @abstractmethod
    def moves(self, **kwargs):
        ...

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

        last_shuffle = None
        for turn in range(turns):
            # We try and generate a new move (which is not the reverse of the preceding!).
            while True:
                move, reverse = random.choices(list(itertools.product(self.moves(), [True, False])))[0]
                if last_shuffle == (move, not reverse):
                    continue

                last_shuffle = (move, reverse)
                break

            log.debug(f"{turn = } shuffling with {move = } {reverse = }")
            shuffled = shuffled.move(move, reverse=reverse)
            path._append(move=move, reverse=reverse)

        return shuffled, path


if __name__ == "__main__":
    pass

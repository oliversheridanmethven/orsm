#!/usr/bin/env python3
"""
A collection of Rubik style shapes we wish to support.
"""

from common.logger import log
from rubik.colours.default_colours import Colours
import numpy as np
from abc import ABC, abstractmethod
from copy import deepcopy
import itertools
import random
from rubik.paths.paths import Path
from rubik.paths.moves import Move


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

    def move(self, *moves, **kwargs):
        if not moves:
            log.info(f"There are no moves specified for {type(self).__name__}")
        moved = type(self)(faces=self.faces, **kwargs)
        for move in moves:
            assert isinstance(move, Move)
            moved = move(shape=moved, **kwargs)
        return moved

    @abstractmethod
    def moves(self, **kwargs):
        ...

    def shuffle(self, *args, turns=100, seed=False, **kwargs):
        """Produces a shuffled cube, and lists how it got there."""
        assert isinstance(turns, int) and turns >= 0, f"Invalid amount of {turns = } specified."
        path = Path(self)
        shuffled = type(self)(faces=self.faces, **kwargs)
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
    from common.cli import setup_standard_parser
    from itertools import product

    parser = setup_standard_parser(description=__doc__)
    parser.add_argument("--single", help="Show single move combinations.", action="store_true")
    parser.add_argument("--double", help="Show double move combinations.", action="store_true")
    parser.add_argument("--shuffle", type=int, metavar="TURNS", help="Show some shuffles.")

    kwargs = vars(parser.parse_args())
    from volume import Volume

    shape = Volume()
    if kwargs["single"]:
        for move in shape.moves():
            log.info(f"Original: {shape.show()}")
            log.info(f"{move}: {shape.move(move).show()}")
            log.info(f"{move} (reversed): {shape.move(move, reverse=True).show()}\n\n")
    if kwargs["double"]:
        for move_1, move_2 in product(*[shape.moves() for i in range(2)]):
            log.info(f"Original: {shape.show()}")
            moved = shape
            for step, move in enumerate([move_1, move_2]):
                log.info(f"{step = } {move}")
                moved = moved.move(move)
                log.info(f"{moved.show()}")
    turns = kwargs["shuffle"]
    if turns:
        shuffled, path = shape.shuffle(turns=turns)
        log.info(f"The target shuffled cube is: {shuffled}")
        log.info(f"Obtained by:")
        for turn, (move, reverse) in enumerate(zip(path.moves, path.reverses)):
            log.info(f"{turn = }: {move} {'in reverse' if reverse else ''}")

        moved = shape
        log.info(f"The starting configuration is: {moved}")
        for turn, (move, reverse) in enumerate(zip(path.moves, path.reverses)):
            log.info(f"{turn = }: {move} {'in reverse' if reverse else ''}")
            moved = moved.move(move, reverse=reverse)
            log.info(f"The moved configuration is: {moved}")
        log.info(f"The final moved configuration is: {moved}")
        log.info(f"The target configuration is: {shuffled}")
        assert moved == shuffled, f"We should have recovered our target configuration."

#!/usr/bin/env python3

from copy import deepcopy
from common.profiling import profile


class Path:
    """Stores a path of moves."""

    def __init__(self, shape, *args, **kwargs):
        self.moves = []
        self.reverses = []
        self.shape = shape
        self._set_path()

    def _set_path(self):
        self.path = {"moves": self.moves, "reverses": self.reverses}

    def _append(self, *args, move, reverse, **kwargs):
        self.moves.append(move)
        self.reverses.append(reverse)

    def pop(self, index=0, /):
        new = type(self)(self.shape)
        new.add(move=self.moves.pop(), reverse=self.reverses.pop())
        return new

    def __add__(self, other):
        new = self.__copy__()
        for move, reverse in zip(other.moves, other.reverses):
            new.moves.append(move)
            new.reverses.append(reverse)
        return new

    def __eq__(self, other):
        return self.path == other.path

    def __len__(self):
        return len(self.moves)

    def __str__(self):
        s = ""
        for move, reverse in zip(self.moves, self.reverses):
            s += f"\n{move} {'in reverse' if reverse else ''}"
        if not s:
            s = "Empty Path"
        else:
            s += "\n"
        return s

    def __reversed__(self):
        new = self.__copy__()
        new.moves = new.moves[::-1]
        new.reverses = [not reverse for reverse in new.reverses[::-1]]
        new._set_path()
        return new

    @profile
    def __copy__(self):
        new = type(self)(self.shape)
        new.moves = deepcopy(self.moves)
        new.reverses = deepcopy(self.reverses)
        new._set_path()
        return new

    @profile
    def add(self, *, move, reverse, **kwargs):
        new = self.__copy__()
        new._append(move=move, reverse=reverse)
        return new


if __name__ == "__main__":
    pass

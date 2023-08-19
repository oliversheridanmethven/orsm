#!/usr/bin/env python3

from abc import ABC, abstractmethod


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

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__doc__


if __name__ == "__main__":
    pass

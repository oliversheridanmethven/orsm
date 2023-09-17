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
        doc_string_description = self.__doc__
        assert doc_string_description is not None and isinstance(doc_string_description, str) and doc_string_description, f"A docstring describing {self = } must be provided and non-trivial, not {doc_string_description = }."
        return doc_string_description

    def __hash__(self):
        # The description should be unique.
        return hash(repr(self))


if __name__ == "__main__":
    pass

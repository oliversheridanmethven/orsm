#!/usr/bin/env python3
"""
A small helper script to convert the tile permutations
specified using the faces syntax into those with array
syntax.
"""

from rubik.shapes import Cube as Shape
from common.logger import log
import numpy as np
from common.cli import standard_parse

"""
To support this functionality, as we are breaking some of our class
variants / type assumptions to work these things out, the call to 
a class's move call operator tends to look like:

def __call__(self, *args, shape, reverse=False, **kwargs):
    array = shape._array
    if not shape._faces:
        shape._update_faces()
    faces = deepcopy(shape._faces)
    if not shape._faces:
        shape._update_faces()
    if not reverse:
        faces[0][1], faces[2][1], faces[1][1], faces[3][1] = faces[3][1], faces[0][1], faces[2][1], faces[1][1]
    else:
        ...
    moved = type(shape)(faces=faces)
    return moved
"""


def permuations_for_each_turn(forward_permutation):
    for turns in [1, 2, 3, 4]:
        index_array = np.array([i for i, _ in enumerate(forward_permutation)])
        permutation_indices = index_array
        for turn in range(turns):
            permutation_indices = permutation_indices[forward_permutation]
        permutation_indices = list(permutation_indices)
        log.print(f"{turn + 1 = }\t{permutation_indices = }")


def combine_permutations(permutations):
    assert len(permutations)
    index_array = np.array([i for i, _ in enumerate(permutations[0])])
    permutation_indices = index_array
    for forward_permutation in permutations:
        permutation_indices = permutation_indices[forward_permutation]
    return list(permutation_indices)


if __name__ == "__main__":
    standard_parse()
    shape = Shape()
    for move in shape.moves():
        forward_permutation = []
        for reverse in [False]:
            log.info(f"The shape starts off looking like: {shape= !s}")
            faces_array = shape.to_array()
            index_array = np.array([i for i, _ in enumerate(faces_array)])
            log.info(f"{faces_array = }, {index_array = }")
            indices = shape.from_array(array=index_array)
            # The faces of indices are correct, but the array is valid.
            moved = indices.move(move, reverse=reverse, copy_faces=True)
            permuted_indices = moved.to_array()
            forward_permutation = list(permuted_indices)
            permuations_for_each_turn(forward_permutation)

    # If we want to combine several:
    permutations = [
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 12, 9, 16, 13, 10, 17, 14, 11, 18, 19, 53, 21, 22, 52, 24, 25, 51, 38, 28, 29, 37, 31, 32, 36, 34, 35, 20, 23, 26, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 27, 30, 33],
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 50, 20, 21, 49, 23, 24, 48, 26, 27, 41, 29, 30, 40, 32, 33, 39, 35, 36, 37, 38, 19, 22, 25, 42, 43, 44, 45, 46, 47, 28, 31, 34, 51, 52, 53],
    ]

    if permutations:
        combined = combine_permutations(permutations)
        permuations_for_each_turn(combined)

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
        for turns in [1, 2, 3, 4]:
            index_array = np.array([i for i, _ in enumerate(forward_permutation)])
            permutation_indices = index_array
            for turn in range(turns):
                permutation_indices = permutation_indices[forward_permutation]
            permutation_indices = list(permutation_indices)
            log.print(f"{turn + 1 = }\t{permutation_indices = }")
            # moved._update_faces()
            # log.info(f"The moved shape looks like: {moved= !s}")

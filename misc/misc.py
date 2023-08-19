from rubik.shapes import Sheet as Shape
from common.logger import log
import numpy as np
from common.cli import standard_parse

if __name__ == "__main__":
    standard_parse()
    shape = Shape()
    for move in shape.moves():
        for reverse in [False, True]:
            faces_array = shape.to_array()
            index_array = np.array([i for i, _ in enumerate(faces_array)])
            log.info(f"{faces_array = }, {index_array = }")
            indices = shape.from_array(array=index_array)
            # The faces of indices are correct, but the array is valid.
            moved = indices.move(move, reverse=reverse, copy_faces=True)
            permuted_indices = moved.to_array()
            forward_permutation = list(permuted_indices)
            log.print(f"{forward_permutation = }")

#!/usr/bin/env python3
"""
Generate shuffles of certain difficulty.
"""

from rubik.solvers.solver import next_generation_of_shapes_with_paths
from rubik.paths.path import Path
from common.logger import log
from common.timing import Timeout


def specific(*args, start, turns, seed=None, timeout=None, **kwargs):
    """A shuffle of a specific difficulty"""

    shapes_and_paths_new = {start: Path(start)}
    shapes_and_paths_encountered = {}

    generation = 0
    with Timeout(timeout=timeout):
        while turns == "god" or generation < turns:
            log.debug(f"{generation = }, we have encountered {len(shapes_and_paths_encountered)} shapes previously")
            shapes_and_paths_encountered = {**shapes_and_paths_encountered, **shapes_and_paths_new}
            shapes_and_paths_new_previous = shapes_and_paths_new
            shapes_and_paths_next_gen = next_generation_of_shapes_with_paths(shapes_and_paths_new)
            shapes_and_paths_new = {shape: path for shape, path in shapes_and_paths_next_gen.items() if shape not in shapes_and_paths_encountered}
            if not shapes_and_paths_new:
                if turns == "god":
                    log.debug(f"We have found a god shuffle after {generation = }")
                    shapes_and_paths_new = shapes_and_paths_new_previous
                    break
                raise RuntimeError(f"The requested difficulty is too hard, and we could not generate any new paths after {generation = } when requesting {turns = }.")
            generation += 1

    log.info(f"We were able to find {len(shapes_and_paths_new)} matching the specific difficulty ({turns = }).")
    shuffled, shuffle_path = shapes_and_paths_new.popitem()
    return shuffled, shuffle_path


def god(*args, **kwargs):
    return specific(*args, turns="god", **kwargs)


if __name__ == "__main__":
    pass

#!/usr/bin/env python3
"""
A collection of solvers.
"""
from common.logger import log
from abc import ABC, abstractmethod
from rubik.shapes.shape import Path, Shape
from common.variables import variable_names_and_objects


class Solver(ABC):
    """
    Solves a Rubik style puzzle.
    """

    @abstractmethod
    def solve(self, *args, start, target, **kwargs):
        ...


class BruteForce(Solver):
    """
    A brute force solver.
    """

    def solve(self, *args, start, target, **kwargs):
        for name, variable in variable_names_and_objects(start, target):
            assert isinstance(variable, Shape), f"{name} is the wrong type."
        assert isinstance(start, type(target)), f"Our two shapes are different: {type(start) = } and {type(target) = }"
        path = Path(start)
        if start == target:
            log.info(f"The start and target are the same.")
            return path

        shapes_and_paths = {start: path}

        while True:
            shapes_and_paths_next = {}
            # We generate the next generation of shapes.
            for shape, path in shapes_and_paths.items():
                for reverse in [True, False]:
                    for move in shape.moves():
                        moved = shape.move(move, reverse=reverse)
                        moved_path = path.add(move=move, reverse=reverse)
                        assert moved_path != path, f"The path has not changed."
                        assert len(moved_path) == len(path) + 1, f"The path has not increased enough."
                        shapes_and_paths_next[moved] = moved_path
            shapes_and_paths = shapes_and_paths_next
            try:
                return shapes_and_paths[target]
            except KeyError as e:
                pass


if __name__ == "__main__":
    pass

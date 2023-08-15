#!/usr/bin/env python3
"""
A collection of solvers.
"""
from common.logger import log
from abc import ABC, abstractmethod
from rubik.shapes.shape import Path, Shape
from common.variables import variable_names_and_objects
from common.logger import progressbar
from common.profiling import profiler, profile


# TODO: move the profiler into my logger tool so it respects the verbosity level...


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

    @profile
    def solve(self, *args, start, target, **kwargs):
        for name, variable in variable_names_and_objects(start, target):
            assert isinstance(variable, Shape), f"{name} is the wrong type."
        assert isinstance(start, type(target)), f"Our two shapes are different: {type(start) = } and {type(target) = }"
        path = Path(start)
        if start == target:
            log.info(f"The start and target are the same.")
            return path

        shapes_and_paths = {start: path}

        turns = 1
        while True:
            shapes_and_paths_next = {}
            # We generate the next generation of shapes.
            log.info(f"Exploring all combinations with {turns = }")
            for shape, path in progressbar(shapes_and_paths.items()):
                # This is the performance bottleneck, and the hotspots are labelled.
                for reverse in [True, False]:
                    for move in shape.moves():
                        moved = shape.move(move, reverse=reverse)  # 8-10%
                        moved_path = path.add(move=move, reverse=reverse)  # 25-30%
                        assert moved_path != path, f"The path has not changed."
                        assert len(moved_path) == len(path) + 1, f"The path has not increased enough."
                        shapes_and_paths_next[moved] = moved_path  # 50-60%
            shapes_and_paths = shapes_and_paths_next
            if target in shapes_and_paths:
                path = shapes_and_paths[target]
                log.info(f"Found the path {path}")
                return path
            turns += 1


if __name__ == "__main__":
    from common.cli import setup_standard_parser
    from rubik.shapes.shape import Volume

    parser = setup_standard_parser(description=__doc__)
    parser.add_argument("--brute_force", help="Demo the brute force solver.", action="store_true")
    parser.add_argument("--shuffle", type=int, metavar="TURNS", help="The amount of turns to do.", default=10)
    parser.add_argument("--seed", type=int, metavar="INT", help="Seed the randomness.")
    parser.add_argument("--profile", help="Enable profiling.", action="store_true")
    kwargs = vars(parser.parse_args())
    if kwargs["brute_force"]:
        if kwargs["profile"]:
            profiler.enable_by_count()
        shape = Volume()
        solver = BruteForce()
        shuffled, shuffle_path = shape.shuffle(turns=kwargs["shuffle"], seed=kwargs["seed"])
        solution_path = solver.solve(start=shape, target=shuffled)
        if kwargs["profile"]:
            profiler.print_stats()

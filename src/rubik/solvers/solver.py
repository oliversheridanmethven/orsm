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
from functools import wraps


# TODO: move the profiler into my logger tool so it respects the verbosity level...


class Solver(ABC):
    """
    Solves a Rubik style puzzle.
    """

    @abstractmethod
    def solve(self, *args, start, target, **kwargs):
        ...


def check_solver_inputs(func):
    """Checks some basic function arguments for a solver and the trivial case."""

    @wraps(func)
    def check_solver_inputs_wrapper(*args, start, target, **kwargs):
        for name, variable in variable_names_and_objects(start, target):
            assert isinstance(variable, Shape), f"{name} is the wrong type."
        assert isinstance(start, type(target)), f"Our two shapes are different: {type(start) = } and {type(target) = }"
        return func(*args, start=start, target=target, **kwargs)

    return check_solver_inputs_wrapper


def next_generation_of_moves(shapes_and_paths):
    """
    Compute the next generation of shapes that can be achieved
    from the input group.
    """
    assert isinstance(shapes_and_paths, dict)
    shapes_and_paths_next = {}
    for shape, path in progressbar(shapes_and_paths.items()):
        assert isinstance(shape, Shape)
        assert isinstance(path, Path)
        for reverse in [True, False]:
            for move in shape.moves():
                moved = shape.move(move, reverse=reverse)
                moved_path = path.add(move=move, reverse=reverse)
                assert moved_path != path, f"The path has not changed."
                assert len(moved_path) == len(path) + 1, f"The path has not increased enough."
                shapes_and_paths_next[moved] = moved_path
    return shapes_and_paths_next


if __name__ == "__main__":
    from common.cli import setup_standard_parser
    from rubik.shapes.shape import Volume

    parser = setup_standard_parser(description=__doc__)
    parser.add_argument("--brute_force", help="Demo the brute force solver.", action="store_true")
    parser.add_argument("--meet_in_middle", help="Demo the meet in the middle solver.", action="store_true")
    parser.add_argument("--shuffle", type=int, metavar="TURNS", help="The amount of turns to do.", default=10)
    parser.add_argument("--seed", type=int, metavar="INT", help="Seed the randomness.")
    parser.add_argument("--profile", help="Enable profiling.", action="store_true")
    kwargs = vars(parser.parse_args())
    if kwargs["profile"]:
        profiler.enable_by_count()
    shape = Volume()
    shuffled, shuffle_path = shape.shuffle(turns=kwargs["shuffle"], seed=kwargs["seed"])
    if kwargs["brute_force"]:
        solution_path = BruteForce().solve(start=shape, target=shuffled)
    if kwargs["meet_in_middle"]:
        solution_path = MeetInMiddle().solve(start=shape, target=shuffled)
    if kwargs["profile"]:
        profiler.print_stats()

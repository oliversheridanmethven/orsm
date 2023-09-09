#!/usr/bin/env python3

from rubik.paths.path import Path
from rubik.solvers.solver import Solver, check_solver_inputs, next_generation_of_shapes_with_paths
from common.logger import log
from common.profiling import profile


class MeetInMiddle(Solver):
    """
    A "meet in the middle" solver.
    """

    @check_solver_inputs
    def solve(self, *args, start, target, **kwargs):

        turns = 0
        shape_and_path_fronts = [{endpoint: Path(endpoint)} for endpoint in [target, start]]
        while True:
            shape_and_path_front_1, shape_and_path_front_2 = shape_and_path_fronts
            if (overlaps := shape_and_path_front_1.keys() & shape_and_path_front_2.keys()):
                log.info(f"We have found {len(overlaps)} solutions with {turns = }.")
                break
            shape_and_path_fronts = shape_and_path_fronts[::-1]
            shape_and_path_fronts[0] = next_generation_of_shapes_with_paths(shape_and_path_fronts[0])
            turns += 1

        shape_and_path_fronts = shape_and_path_fronts if turns % 2 != 0 else reversed(shape_and_path_fronts)
        overlap = overlaps.pop()
        log.debug(f"The item that overlaps from both sets is {overlap = !s}")
        starting_path, finishing_path = [front[overlap] for front in shape_and_path_fronts]
        finishing_path = reversed(finishing_path)
        total_path = starting_path + finishing_path
        assert len(total_path) == turns, f"Our {total_path = } consists of more {turns = } than we have counted."
        log.debug(f"The starting_path = \n{starting_path}\nand finishing_path = \n{finishing_path}")
        log.info(f"The solution path we have found was: {total_path}")
        return total_path


if __name__ == "__main__":
    pass

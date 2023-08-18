#!/usr/bin/env python3
import logging
import unittest
from rubik.shapes import shape as Shape
from rubik.solvers.solver import BruteForce, MeetInMiddle
from common.cli import unit_test_parse
from common.variables import variable_names_and_objects
from common.logger import log


class Solvers(unittest.TestCase):
    def test_solvers(self):
        for name, Solver in variable_names_and_objects(BruteForce, MeetInMiddle):
            solver = Solver()
            shape = Shape.Volume()
            for turns in range(5):
                shuffled, shuffle_path = shape.shuffle(turns=turns, seed=0)
                solution_path = solver.solve(start=shape, target=shuffled)
                self.assertLessEqual(len(solution_path.moves), len(shuffle_path), f"The solution path for {name} is not optimal, as it takes more moves than we used to shuffle our cube.")
                solution = shape
                for move, reverse in zip(solution_path.moves, solution_path.reverses):
                    solution = solution.move(move, reverse=reverse)
                log.debug(f"We are comparing: {solution = !s}{shuffled = !s}")
                self.assertEqual(solution, shuffled, f"Using {name} we do not arrive at the target using the solution moves.")
                solution = shuffled
                for move, reverse in reversed(list(zip(solution_path.moves, solution_path.reverses))):
                    other_direction = not reverse
                    solution = solution.move(move, reverse=other_direction)
                self.assertEqual(solution, shape, f"Using {name} we do not arrive at the start using the solution moves in reverse.")


if __name__ == '__main__':
    unit_test_parse()
    unittest.main()

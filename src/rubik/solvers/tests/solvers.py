#!/usr/bin/env python3
import logging
import unittest
from rubik import shapes
from rubik.solvers import BruteForce, MeetInMiddle, MeetInMiddleRecursive
from common.cli import unit_test_parse
from common.variables import variable_names_and_objects
from common.logger import log
from common.timing import Timeout


class Solvers(unittest.TestCase):

    def setUp(self):
        self.names_and_solvers = variable_names_and_objects(BruteForce, MeetInMiddle, MeetInMiddleRecursive)

    def _check_solution_recovers_shuffled(self, *args, original, shuffled, solution_path, shuffle_path, solver_name, **kwargs):
        solution = original
        for move, reverse in zip(solution_path.moves, solution_path.reverses):
            solution = solution.move(move, reverse=reverse)
        log.debug(f"We are comparing: {solution = !s}{shuffled = !s}")
        self.assertEqual(solution, shuffled, f"Using {solver_name} we do not arrive at the target using the solution moves.")
        solution = shuffled
        for move, reverse in reversed(list(zip(solution_path.moves, solution_path.reverses))):
            other_direction = not reverse
            solution = solution.move(move, reverse=other_direction)
        self.assertEqual(solution, original, f"Using {solver_name} we do not arrive at the start using the solution moves in reverse.")

    def test_solvers(self):
        for name, Solver in self.names_and_solvers:
            solver = Solver()
            shape = shapes.Volume()
            for turns in range(4):
                with Timeout(5):
                    shuffled, shuffle_path = shape.shuffle(turns=turns, seed=0)
                    solution_path = solver.solve(start=shape, target=shuffled)
                    self.assertLessEqual(len(solution_path.moves), len(shuffle_path), f"The solution path for {name} is not optimal, as it takes more moves than we used to shuffle our cube.")
                    self._check_solution_recovers_shuffled(original=shape, shuffled=shuffled, solution_path=solution_path, shuffle_path=shuffle_path, solver_name=name)

    def test_solver_at_specific_difficulty(self):
        for name, Solver in self.names_and_solvers:
            solver = Solver()
            shape = shapes.Volume()
            from rubik.shuffles.difficulty import specific
            for turns in range(4):
                with Timeout(5):
                    shuffled, shuffle_path = specific(start=shape, turns=turns, seed=0)
                    self.assertEqual(len(shuffle_path), turns, f"We have not generated a shuffled path with the required number of turns.")
                    solution_path = solver.solve(start=shape, target=shuffled)
                    self.assertLessEqual(len(solution_path.moves), len(shuffle_path), f"The solution path for {name} is not optimal, as it takes more moves than we used to shuffle our cube.")
                    self.assertEqual(len(solution_path.moves), turns, f"Our solution path is not the right length.")
                    self._check_solution_recovers_shuffled(original=shape, shuffled=shuffled, solution_path=solution_path, shuffle_path=shuffle_path, solver_name=name)


if __name__ == '__main__':
    unit_test_parse()
    unittest.main()

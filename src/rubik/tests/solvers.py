#!/usr/bin/env python3
import unittest
from rubik.shapes import shape as Shape
from rubik.solvers.solver import BruteForce
from common.cli import unit_test_parse


class Solvers(unittest.TestCase):
    def test_brute_force(self):
        solver = BruteForce()
        shape = Shape.Volume()
        for turns in range(6):
            shuffled, shuffle_path = shape.shuffle(turns=turns, seed=0)
            solution_path = solver.solve(start=shape, target=shuffled)
            self.assertLessEqual(len(solution_path.moves), len(shuffle_path), f"The solution path is not optimal, as it takes more moves than we used to shuffle our cube.")
            solution = shape
            for move, reverse in zip(solution_path.moves, solution_path.reverses):
                solution = solution.move(move, reverse=reverse)
            self.assertEqual(solution, shuffled, f"We do not arrive at the target using the solution moves.")
            solution = shuffled
            for move, reverse in reversed(list(zip(solution_path.moves, solution_path.reverses))):
                other_direction = not reverse
                solution = solution.move(move, reverse=other_direction)
            self.assertEqual(solution, shape, f"We do not arrive at the start using the solution moves in reverse.")


if __name__ == '__main__':
    unit_test_parse()
    unittest.main()

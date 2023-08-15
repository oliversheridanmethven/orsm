#!/usr/bin/env python3
import unittest
from rubik.shapes import shape as Shape


class Solvers(unittest.TestCase):
    def test_brute_force(self):
        solver = brute_force()

        shape = Shape.Volume()
        shuffled = shape
        solver.solve(start)
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unit_test_parse()
    unittest.main()

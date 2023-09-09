#!/usr/bin/env python3
import unittest
from rubik.shufflers.shufflers import specific, god
from rubik.shapes import Domino, Volume, Square, Sheet
from common.variables import variable_names_and_objects
from common.logger import log
from common.timing import Timeout


class Shuffles(unittest.TestCase):

    def test_trivial_difficulty(self):
        for name, Shape in variable_names_and_objects(Domino, Volume):
            shape = Shape()
            log.debug(f"Testing the shape {name}")
            turns = 0
            shuffled, shuffle_path = specific(start=shape, turns=turns, seed=0)
            self.assertEqual(shuffled, shape)
            self.assertEqual(len(shuffle_path), turns)

    def test_feasible_easy_difficulty(self):
        for name, Shape in variable_names_and_objects(Domino, Volume):
            shape = Shape()
            log.debug(f"Testing the shape {name}")
            for turns in range(1, 2):
                shuffled, shuffle_path = specific(start=shape, turns=turns, seed=0)
                self.assertNotEqual(shuffled, shape)
                self.assertEqual(len(shuffle_path), turns)

    def test_feasible_moderate_difficulty(self):
        shape = Volume()
        for turns in range(1, 5):
            with Timeout(5):
                shuffled, shuffle_path = specific(start=shape, turns=turns, seed=0)
                self.assertNotEqual(shuffled, shape)
                self.assertEqual(len(shuffle_path), turns)

    def test_infeasible_moderate_difficulty(self):
        shape = Domino()
        turns = 2
        with self.assertRaises(RuntimeError, msg="We should not have been able to produce a difficulty this large."):
            shuffled, shuffle_path = specific(start=shape, turns=turns, seed=0)

    def test_easy_god_shuffle(self):
        shape = Domino()
        god_turns = 1
        with Timeout(5):
            shuffled, shuffle_path = god(start=shape, seed=0)
            self.assertNotEqual(shuffled, shape)
            self.assertEqual(len(shuffle_path), god_turns)

    ##########################################################
    # Some of the following God numbers are my best guesses...
    ##########################################################

    def test_mild_god_shuffle(self):
        shape = Square()
        god_turns = 2
        with Timeout(5):
            shuffled, shuffle_path = god(start=shape, seed=0)
            self.assertNotEqual(shuffled, shape)
            self.assertEqual(len(shuffle_path), god_turns)

    def test_moderate_god_shuffle(self):
        shape = Sheet()
        god_turns = 3
        with Timeout(5):
            shuffled, shuffle_path = god(start=shape, seed=0)
            self.assertNotEqual(shuffled, shape)
            self.assertEqual(len(shuffle_path), god_turns)

    @unittest.skip("This takes too long to compute (e.g. O(30+ mins)).")
    def test_moderate_god_shuffle(self):
        shape = Volume()
        god_turns = 11  # cf: https://ruwix.com/the-rubiks-cube/gods-number/
        with Timeout(10):
            shuffled, shuffle_path = god(start=shape, seed=0)
            self.assertNotEqual(shuffled, shape)
            self.assertEqual(len(shuffle_path), god_turns)


if __name__ == '__main__':
    from common.cli import unit_test_parse

    unit_test_parse()
    unittest.main()

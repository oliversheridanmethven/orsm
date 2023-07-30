#!/usr/bin/env python3

import sys

print(sys.path)

import unittest
import time
from common.timing import time_function, timeout, TimeoutError


class TimeoutHandler(unittest.TestCase):

    def test_raises_error(self):
        with self.assertRaises(TimeoutError):
            with timeout(limit=1):
                time.sleep(2)

    def test_bad_values(self):
        for value in [-1, 0, timeout.max_limit + 1]:
            with self.assertRaises(AssertionError):
                timeout(limit=value)

    def test_allowed_values(self):
        for value in [-1, timeout.max_limit + 1]:
            with self.assertRaises(AssertionError):
                timeout(limit=value)


class TimingFunction(unittest.TestCase):

    def setUp(self):
        self.function = time.sleep

    def test_return_type(self):
        with timeout(limit=10):
            name = "sleep test"
            duration = 0.1
            results = time_function(duration, name=name, function=self.function, iter_limit=5, time_limit=5, suppress_output=False)
            expected = {"name": name, "seconds": 3, "total_iterations": 3, "average": 1}
            for key, value in results.items():
                self.assertIn(key, expected.keys())


if __name__ == '__main__':
    unittest.main()

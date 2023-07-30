#!/usr/bin/env python3

import sys

print(sys.path)

import unittest
import time
from common.timing import time_function


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.function = time.sleep

    # def test_return_type(self):
    #     name = "sleep test"
    #     duration = 1
    #     results = time_function(duration, name=name, function=self.function, iter_limit=3, time_limit=10, suppress_output=True)
    #     expected = {"name": name, "seconds": 3, "total_iterations": 3, "average": 1}
    #     for key, value in results:
    #         self.assertIn(key, expected.keys())


if __name__ == '__main__':
    unittest.main()

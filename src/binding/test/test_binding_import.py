#!/usr/bin/env python3
"""
Testing the binding module.
"""

import unittest
import binding


class TestBindings(unittest.TestCase):
    def test_bound_functions_run(self):
        binding.hello_world()
        binding.foo(1,'foo')

    # def test_fail(self):
    #     # TODO: Figure out how to get this test to work properly.
    #     self.assertRaises(SystemExit, binding.fail)


if __name__ == '__main__':
    unittest.main()

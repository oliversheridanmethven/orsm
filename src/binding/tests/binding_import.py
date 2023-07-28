#!/usr/bin/env python3
"""
Testing the binding module.
"""

import unittest
import binding
import multiprocessing as mp


class Bindings(unittest.TestCase):
    def test_bound_functions_run(self):
        binding.hello_world()
        binding.foo(1,'foo')

    def test_fatal_failure(self):
        # Tests which expect an exit from a C extension must be launched in a sub process,
        # else it will take down the Python interpretor session with it.
        # cf. https://stackoverflow.com/a/73070027/5134817
        ps = mp.Process(target=binding.fatal_failure)
        ps.start()
        ps.join()
        self.assertNotEqual(ps.exitcode, 0, "The exit code from the failing process should not be 0.")


if __name__ == '__main__':
    unittest.main()

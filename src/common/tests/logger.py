#!/usr/bin/env python3

import io
import unittest
from contextlib import redirect_stdout
from common.logger import log, set_logging_level
from common.variables import variable_names_and_objects
import logging
import sys

from testfixtures import LogCapture
import subprocess
import shlex


class Logger(unittest.TestCase):
    def test_regular_output(self):
        names_and_messages = {}
        with LogCapture(level=log.PRINT) as l:
            for name, logger in variable_names_and_objects(log.trace, log.debug, log.info, log.print, log.warning, log.error, log.critical):
                message = f"A message from {name}"
                logger(message)
                if log.getLevelNamesMapping()[name.upper()] >= log.PRINT:
                    names_and_messages[name] = message
        l.check(*[('root', name.upper(), message) for name, message in names_and_messages.items()])

    def test_all_output(self):
        names_and_messages = {}
        with LogCapture() as l:
            set_logging_level(level=log.TRACE)
            for name, logger in variable_names_and_objects(log.trace, log.debug, log.info, log.print, log.warning, log.error, log.critical):
                message = f"A message from {name}"
                logger(message)
                names_and_messages[name] = message
        l.check(*[('root', name.upper(), message) for name, message in names_and_messages.items()])

    def test_output_from_cli_trace(self):
        from subprocess import Popen, PIPE
        p = Popen(["python", "cli_print_logs.py", *shlex.split("--trace")], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(b"")
        rc = p.returncode
        assert rc == 0, "We were unable to run the subprocess."
        all_output = "".join([i.decode() for i in [output, err]])
        for name, logger in variable_names_and_objects(log.trace, log.debug, log.info, log.print, log.warning, log.error, log.critical):
            message = f"A message from {name}"
            self.assertIn(message, all_output)

    def test_output_from_cli(self):
        # Run the other script
        # subprocess.run(["python", "cli_print_logs.py", shlex.split("--verbose")])
        # subprocess.run(["python", "cli_print_logs.py", shlex.split("--trace")])
        # subprocess.run(["python", "cli_print_logs.py", shlex.split("--debug")])
        raise NotImplemented


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3

import io
import unittest
from contextlib import redirect_stdout
from common.logger import log, set_logging_level, log_file_extensions
from common.variables import variable_names_and_objects
import logging
import sys
from subprocess import Popen, PIPE
import cli_print_logs
from testfixtures import LogCapture
import subprocess
import shlex
from tempfile import TemporaryDirectory
import os
import pathlib


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


class LoggerVerbosity(unittest.TestCase):

    def test_output_from_cli_regular(self):
        p = Popen(["python", f"{cli_print_logs.__file__}"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(b"")
        rc = p.returncode
        self.assertEqual(rc, 0, f"We were unable to run the subprocess, encountering\noutput:\n{output=}\nerror:\n{err}")
        for name, logger in variable_names_and_objects(log.trace, log.debug, log.info, log.print, log.warning, log.error, log.critical):
            message = f"A message from {name}"
            if log.getLevelNamesMapping()[name.upper()] > log.DEFAULT_LEVEL:
                self.assertIn(message, err.decode())
            elif log.getLevelNamesMapping()[name.upper()] == log.DEFAULT_LEVEL:
                self.assertIn(message, output.decode())
            else:
                self.assertNotIn(message, output.decode())
                self.assertNotIn(message, err.decode())

    def test_output_from_cli_level(self):
        flags_and_levels = {"--trace": log.TRACE,
                            "--verbose": log.INFO,
                            "--debug": log.DEBUG,
                            "--quiet": log.WARNING,
                            "--silent": log.ERROR}
        for flag, level in flags_and_levels.items():
            p = Popen(["python", f"{cli_print_logs.__file__}", *shlex.split(flag)], stdin=PIPE, stdout=PIPE, stderr=PIPE)
            output, err = p.communicate(b"")
            rc = p.returncode
            self.assertEqual(rc, 0, f"We were unable to run the subprocess with {flag = }, encountering\noutput:\n{output=}\nerror:\n{err}")
            all_output = "".join([i.decode() for i in [output, err]])
            for name, logger in variable_names_and_objects(log.trace, log.debug, log.info, log.print, log.warning, log.error, log.critical):
                message = f"A message from {name}"
                if log.getLevelNamesMapping()[name.upper()] >= level:
                    self.assertIn(message, all_output)
                else:
                    self.assertNotIn(message, all_output)

    def test_no_output_when_suppressed(self):
        p = Popen(["python", f"{cli_print_logs.__file__}", *shlex.split("--suppress_console_output")], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(b"")
        rc = p.returncode
        self.assertEqual(rc, 0, f"We were unable to run the subprocess, encountering\noutput:\n{output=}\nerror:\n{err}")
        self.assertFalse(output)
        self.assertFalse(err)

    def test_output_files_produced(self):
        file_names = ["", "foo"]
        for file_name in file_names:
            with TemporaryDirectory() as temp_directory:
                os.chdir(temp_directory)
                expected_files = [f"{file_name}{extension}" for extension in log_file_extensions.values()]
                p = Popen(["python", f"{cli_print_logs.__file__}", *shlex.split(f"--trace --log_files {file_name}")], stdin=PIPE, stdout=PIPE, stderr=PIPE, cwd=temp_directory)
                output, err = p.communicate(b"")
                rc = p.returncode
                self.assertEqual(rc, 0, f"We were unable to run the subprocess, encountering\noutput:\n{output=}\nerror:\n{err}")
                for expected_file in expected_files:
                    file_path = pathlib.Path(expected_file)
                    self.assertTrue(file_path.is_file(), f"We cant find the file: {file_path}")
                    self.assertGreater(os.path.getsize(file_path), 0, f"The {file_path = } is expected to be non-empty.")


if __name__ == '__main__':
    unittest.main()

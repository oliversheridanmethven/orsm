#!/usr/bin/env python3
"""
Some wrapping around the default logging module.
"""

import logging
from common.variables import variable_names_and_objects
import sys
from haggis.logs import add_logging_level
from termcolor import colored

add_logging_level('TRACE', logging.DEBUG - 5)
add_logging_level('PRINT', logging.WARNING - 5)


class MyFormatter(logging.Formatter):
    """A nice formatter for logging messages."""
    line_formatting = f" {colored('(%(pathname)s:%(lineno)d)', 'light_grey')}"
    timestamp_formatting = f"{colored('[%(asctime)s]: ', 'green')}"
    trace_format = f"{colored('TRACE', 'cyan')}: %(msg)s"
    debug_format = f"{colored('DEBUG', 'magenta')}: %(msg)s"
    info_format = f"{colored('INFO', 'blue')}: %(msg)s"
    print_format = f"%(msg)s"
    warning_format = f"{timestamp_formatting}{colored('WARNING', 'yellow')}:{line_formatting} %(msg)s"
    error_format = f"{timestamp_formatting}{colored('ERROR', 'red')}:{line_formatting} %(msg)s"
    critical_format = f"{timestamp_formatting}{colored('CRITICAL', 'red', attrs=['reverse', 'blink', 'bold'])}: {line_formatting} %(msg)s"

    def __init__(self):
        super().__init__(fmt=f"UNKNOWN: %(msg)s", datefmt=None, style='%')

    def format(self, record):

        # Save the original format configured by the user
        # when the logger formatter was instantiated
        format_orig = self._style._fmt

        # Replace the original format with one customized by logging level
        if record.levelno == logging.TRACE:
            self._style._fmt = MyFormatter.trace_format
        elif record.levelno == logging.DEBUG:
            self._style._fmt = MyFormatter.debug_format
        elif record.levelno == logging.INFO:
            self._style._fmt = MyFormatter.info_format
        elif record.levelno == logging.PRINT:
            self._style._fmt = MyFormatter.print_format
        elif record.levelno == logging.WARNING:
            self._style._fmt = MyFormatter.warning_format
        elif record.levelno == logging.ERROR:
            self._style._fmt = MyFormatter.error_format
        elif record.levelno == logging.CRITICAL:
            self._style._fmt = MyFormatter.critical_format
        else:
            raise NotImplementedError(f"We don't know how to format logging levels: {record.levelno}")

        # Call the original formatter class to do the grunt work
        result = logging.Formatter.format(self, record)

        # Restore the original format configured by the user
        self._style._fmt = format_orig

        return result


# fmt = MyFormatter()
# stdout_handler = logging.StreamHandler(sys.stdout)
# stdout_handler.setFormatter(fmt)
# logging.root.addHandler(stdout_handler)
# stderr_handler = logging.StreamHandler(sys.stderr)
# stderr_handler.setFormatter(fmt)
# logging.root.addHandler(stderr_handler)


class StdOutFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno <= logging.PRINT


class StdErrFilter(logging.Filter):
    def filter(self, rec):
        stdout_filter = StdOutFilter()
        return not stdout_filter.filter(rec)


fmt = MyFormatter()
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setFormatter(fmt)
stdout_handler.addFilter(StdOutFilter())
logging.root.addHandler(stdout_handler)
stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setFormatter(fmt)
stderr_handler.addFilter(StdErrFilter())
logging.root.addHandler(stderr_handler)

log = logging


def set_logging_level(*, level):
    log.root.setLevel(level)


set_logging_level(level=logging.PRINT)

if __name__ == "__main__":
    # A very small demo.
    from time import sleep

    set_logging_level(level=logging.TRACE)
    for name, logger in variable_names_and_objects(log.trace, log.debug, log.info, log.print, log.warning, log.error, log.critical):
        sleep(0.01)  # So we can see the timestamp increments more clearly.
        logger(f"A message from {name}")

#!/usr/bin/env python3
"""
Tools for constructing the CLI
"""

import argparse
from common.logger import log


class HelpFormatter(argparse.RawDescriptionHelpFormatter, argparse.ArgumentDefaultsHelpFormatter):
    pass


def setup_standard_parser(*args, **kwargs):
    parser = argparse.ArgumentParser(*args, **kwargs, formatter_class=HelpFormatter, allow_abbrev=False)
    # How we want to control the logging.
    parser.add_argument("--trace", help="Enable program tracing. Extremely verbose!", action="store_true")
    parser.add_argument("--verbose", help="Enable verbose logging. Very verbose!", action="store_true")
    parser.add_argument("--debug", help="Enable debug logging. Quite verbose!", action="store_true")
    parser.add_argument("--silent", help="Suppress most logging and output. Quite quiet!", action="store_true")
    parser.add_argument("--quiet", help="Supress all logging. Extremely quiet!", action="store_true")
    parser.add_argument("--log_files", type=str, metavar="FILENAME", help="Store log output to files. Split into regular output and error output.")
    # Other common things:
    parser.add_argument("--version", help="Show the version of this program.", action="store_true")

    # TODO: Add version, epilogue, debug, verbose, quiet, silent, log to files, etc.
    return parser

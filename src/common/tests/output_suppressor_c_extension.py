#!/usr/bin/env python3

"""
Testing whether the suppressor appears to work
without relying on nested Python capturing for
a C hello world extension library.
"""

from binding import hello_world as hello_world_c_extension
import argparse
from common.output import Suppressor

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suppress_output", help="Whether to try and suppress the output.", action='store_true')
    kwargs = vars(parser.parse_args())
    with Suppressor(**kwargs):
        hello_world_c_extension()

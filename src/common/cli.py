#!/usr/bin/env python3
"""
Tools for constructing the CLI
"""

import argparse


def setup_standard_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trace", help="Enable program tracing. Extremely verbose!", action="store_true")
    return parser

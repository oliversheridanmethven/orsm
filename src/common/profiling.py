#!/usr/bin/env python3
"""
Some basic profiling tools.

This is largely copied from: https://medium.com/uncountable-engineering/pythons-line-profiler-32df2b07b290
"""

from line_profiler import LineProfiler
from functools import wraps
import inspect
from logger import log as logging


def is_in_debugger():
    # Taken from https://stackoverflow.com/a/338391/5134817
    for frame in inspect.stack():
        if frame[1].endswith("pydevd.py"):
            return True
    return False


profiler = LineProfiler()


def profile(func):
    @wraps(func)
    def profiled_function(*args, **kwargs):
        profiler.add_function(func)
        profiler.enable_by_count()
        return func(*args, **kwargs)

    if not is_in_debugger():
        return profiled_function
    else:
        # The debugger used in e.g. Pycharm requires sys.settrace (cf. https://github.com/pyutils/line_profiler/issues/276), but that's what LineProfiler uses and it upsets everything, so we disable this in debug mode.
        logging.warning(f"We are not profiling the time of the function {func.__name__} ({inspect.getfile(func)}:{inspect.getsourcelines(func)[-1]}).")
        return func


if __name__ == "__main__":
    @profile
    def some_example():
        import time
        for i in range(5):
            time.sleep(0.1)


    some_example()
    profiler.print_stats()

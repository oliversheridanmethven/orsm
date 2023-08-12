#!/usr/bin/env python3
"""
Some basic profiling tools.

This is largely copied from: https://medium.com/uncountable-engineering/pythons-line-profiler-32df2b07b290
"""

from line_profiler import LineProfiler

profiler = LineProfiler()


def profile(func):
    def inner(*args, **kwargs):
        profiler.add_function(func)
        profiler.enable_by_count()
        return func(*args, **kwargs)

    return inner


if __name__ == "__main__":
    @profile
    def some_example():
        import time
        for i in range(5):
            time.sleep(0.1)


    some_example()
    profiler.print_stats()

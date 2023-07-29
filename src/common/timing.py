#!/usr/bin/env python3

"""
Timing functionality.
"""

import time
from common.output import Suppressor


def time_function(*args, name=None, function, iter_limit=None, time_limit=None, suppress_output=False, verbose=True, **kwargs):
    """A basic function timer."""
    name = name if name else function.__name__
    total_iterations = 0
    iterations = 1
    seconds = 0

    if not iter_limit and not time_limit:
        time_limit = 0.1

    with Suppressor(suppress_output=suppress_output):
        while (time_limit and seconds < time_limit) or (iter_limit and total_iterations < iter_limit):
            remaining_iterations = iterations if not iter_limit else min(iterations, iter_limit - total_iterations)
            start = time.time()  # We include the for loop in our timing, hoping it is negligible.
            for i in range(remaining_iterations):
                function(*args, **kwargs)
            end = time.time()
            seconds += end - start
            total_iterations += remaining_iterations
            iterations *= 2
    average = seconds / total_iterations
    if verbose:
        print(f"The function {name} took {seconds} seconds over {total_iterations} iterations, averaging {average} seconds per function call.")
    return {"name": name, "seconds": seconds, "total_iterations": total_iterations, "average": average}

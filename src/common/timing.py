#!/usr/bin/env python3

"""
Timing functionality.
"""

import time
from common.output import Suppressor
from common.variables import variable_names_and_objects
import signal


class timeout:
    """
    A nice timeout handler for with statements.
    Taken from: https://stackoverflow.com/a/49567288/5134817
    also cf: https://www.youtube.com/watch?v=vGWSdp9dyhI

    TODO: Make this into a nice decorator...
    """

    max_limit = 60  # Anything more than this is a ridiculous code smell.

    def __init__(self, *, limit=None, error_message=None):
        if error_message is None:
            error_message = 'Timed out after {} seconds.'.format(limit)
        if limit is not None:
            assert isinstance(limit, int) and 0 < limit <= self.max_limit, f"The timeout {limit = } is not valid."
        self.limit = limit
        self.error_message = error_message

    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)

    def __enter__(self):
        if self.limit:
            self.orig_handler = signal.signal(signal.SIGALRM, self.handle_timeout)
            signal.alarm(self.limit)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.limit:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, self.orig_handler)


class TimeoutError(Exception):
    pass


def time_function(*args, name=None, function, iter_limit=None, time_limit=None, max_time_limit=None, suppress_output=False, verbose=True, **kwargs):
    """A basic function timer."""
    name = name if name else function.__name__
    total_iterations = 0
    iterations = 1
    seconds = 0

    for variable, value in variable_names_and_objects(iter_limit, time_limit, max_time_limit):
        if value:
            assert isinstance(value, int) and 1 <= value, f"The {variable = } has an invalid {value = }"

    if not iter_limit and not time_limit:
        time_limit = max_time_limit if max_time_limit else 0.1

    iteration_growth_factor = 2
    if not max_time_limit and time_limit:
        max_time_limit = 2 * iteration_growth_factor * time_limit

    with timeout(limit=max_time_limit):
        with Suppressor(suppress_output=suppress_output):
            while (time_limit and seconds < time_limit) or (iter_limit and total_iterations < iter_limit):
                remaining_iterations = iterations if not iter_limit else min(iterations, iter_limit - total_iterations)
                start = time.time()  # We include the for loop in our timing, hoping it is negligible.
                if not remaining_iterations:
                    break
                for i in range(remaining_iterations):
                    function(*args, **kwargs)
                end = time.time()
                seconds += end - start
                total_iterations += remaining_iterations
                iterations *= iteration_growth_factor
                iterations = int(iterations)
                assert iterations, "There are no iterations to be done."
    average = seconds / total_iterations
    if verbose:
        print(f"The function {name} took {seconds} seconds over {total_iterations} iterations, averaging {average} seconds per function call.")
    return {"name": name, "seconds": seconds, "total_iterations": total_iterations, "average": average}

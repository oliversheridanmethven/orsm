"""
An example script to benchmark the performance of doing something in Pure
Python versus using a C binding.
"""

from binding import foo_pure_c
from binding.example import foo as foo_pure_python
import timeit
from varname import argname


def get_variale_names_and_objects(*variables):
    """
    Takes the variables input to a function and returns a dict of
    their names and the underlying objects.

    This is ideal for iterating through a list of variables and
    keeping their names:
    e.g.

    a,b,c = 1,2,3
    for name, variable in get_varibale_names_and_objects(a,b,c):
        print(name, variable)

    returns:

    a, 1
    b, 2
    c, 3

    This is particularly useful when a function or class has been
    renamed on an import to a new variable:
    e.g.

    from foo import bar as baz

    the __name__ of baz is still bar, and this function resolves that.
    """
    names = argname('variables')
    return dict(zip(names, variables))


def time_function(*args, name=None, func, iter_limit=None, time_limit=None, suppress_output=False, **kwargs):
    """A basic function timer."""
    import py
    name = name if name else func.__name__
    total_iterations = 0
    iterations = 1
    seconds = 0

    if not iter_limit and not time_limit:
        time_limit = 0.1

    if suppress_output:
        capture = py.io.StdCaptureFD()

    while (time_limit and seconds < time_limit) or (iter_limit and total_iterations < iter_limit):
        import time
        remaining_iterations = iterations if not iter_limit else min(iterations, iter_limit - total_iterations)
        start = time.time()  # We include the for loop in our timing, hoping it is negligible.
        for i in range(remaining_iterations):
            func(*args, **kwargs)
        end = time.time()
        seconds += end - start
        total_iterations += remaining_iterations
        iterations *= 2

    if suppress_output:
        capture.reset()
    print(f"The function {name = } took {seconds = } over {total_iterations = } averaging {seconds/total_iterations} seconds per function call.")


if __name__ == '__main__':
    a = 1
    foo_pure_c(a, b='c')
    foo_pure_python(a, b='python')
    for name, func in get_variale_names_and_objects(foo_pure_c, foo_pure_python).items():
        time_function(a, b=name, name=name, func=func, suppress_output=True)

"""
An example script to benchmark the performance of doing something in Pure
Python versus using a C binding.
"""

from binding import foo_pure_c
from binding import foo_pure_python


if __name__ == '__main__':
    a = 1
    b = "hello from example script"
    foo_c_binding(a, b)
    foo_pure_python(a, b)
"""
An example script to benchmark the performance of doing something in pure
Python versus using a C binding.
"""

from binding import foo as foo_pure_c
from binding.example import foo as foo_pure_python
from common.variables import variable_names_and_objects
from common.timing import time_function

if __name__ == '__main__':
    a = 1
    foo_pure_c(a, b='c')
    foo_pure_python(a, b='python')
    for name, function in variable_names_and_objects(foo_pure_c, foo_pure_python).items():
        time_function(a, b=name, name=name, function=function, suppress_output=True)

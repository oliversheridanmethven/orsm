from varname import argname
from varname.helpers import jsobj
from functools import wraps
import unittest


def jsobj_to_be_wrapped(*args, vars_only=True, **kwargs):
    argnames = argname("args", vars_only=vars_only, frame=2)
    out = dict(zip(argnames, args))
    out.update(kwargs)
    return out


def return_dict_items(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).items()
    return wrapper

class TestWrapper(unittest.TestCase):
    def test_wrapper(self):
        foo = return_dict_items(jsobj_to_be_wrapped)
        a = 1
        self.assertEqual([("a", 1)], list(foo(a)))


if __name__ == '__main__':
    unittest.main()
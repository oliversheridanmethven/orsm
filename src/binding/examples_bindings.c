#define PY_SSIZE_T_CLEAN
#include "examples.h"
#include <Python.h>
#include <stdio.h>

/* Python bindings */

PyObject *_hello_world(PyObject *self, PyObject *args, PyObject *kwargs)
{
    hello_world();
    Py_RETURN_NONE;
}

PyObject *_foo(PyObject *self, PyObject *args, PyObject *kwargs)
{
    /* This is the python equivalent of: def foo(a, b="default", **kwargs): ...  */
    static char *keywords[] = {"a", "b", NULL};
    //    PyObject *_a;
    /* Integers in Python are stored as a long, whereas in C I want an int. Hence we might need
     * to do some error checking or handling if we permit very long ints to be entered. */
    int a;
    char *b = "default";

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "i|s:_foo", keywords, &a, &b))
    {
        /* The arguments passed don't correspond to the signature described. */
        return NULL;
    }
    //    a = PyLong_AsLong(_a);
    foo(a, b);
    return PyLong_FromLong(a);
}

PyObject *_fail(PyObject *self, PyObject *args, PyObject *kwargs)
{
    fail();
    Py_RETURN_NONE;
}

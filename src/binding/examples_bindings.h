#ifndef TESTING_EXAMPLES_BINDINGS_H
#define TESTING_EXAMPLES_BINDINGS_H

#include <Python.h>

PyObject *_hello_world(PyObject *self, PyObject *args, PyObject *kwargs);

PyObject *_foo(PyObject *self, PyObject *args, PyObject *kwargs);

PyObject *_fail(PyObject *self, PyObject *args, PyObject *kwargs);

#endif//TESTING_EXAMPLES_BINDINGS_H

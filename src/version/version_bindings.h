#ifndef TESTING_VERSION_BINDINGS_H
#define TESTING_VERSION_BINDINGS_H

#include <Python.h>

PyObject *_name(PyObject *self, PyObject *args, PyObject *kwargs);

PyObject *_version(PyObject *self, PyObject *args, PyObject *kwargs);

PyObject *_author(PyObject *self, PyObject *args, PyObject *kwargs);

PyObject *_email(PyObject *self, PyObject *args, PyObject *kwargs);

#endif //TESTING_VERSION_BINDINGS_H

#ifndef TESTING_VERSION_BINDINGS_H
#define TESTING_VERSION_BINDINGS_H

#include <Python.h>

PyObject *_repo_name(PyObject *self, PyObject *args, PyObject *kwargs);

PyObject *_repo_version(PyObject *self, PyObject *args, PyObject *kwargs);

PyObject *_repo_author(PyObject *self, PyObject *args, PyObject *kwargs);

PyObject *_repo_email(PyObject *self, PyObject *args, PyObject *kwargs);

#endif //TESTING_VERSION_BINDINGS_H

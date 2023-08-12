#include "version_bindings.h"
#include "version.h"


PyObject *_repo_name(PyObject *self, PyObject *args, PyObject *kwargs) {
    return PyUnicode_FromString(repo_name());
}

PyObject *_repo_version(PyObject *self, PyObject *args, PyObject *kwargs) {
    return PyUnicode_FromString(repo_version());
}

PyObject *_repo_author(PyObject *self, PyObject *args, PyObject *kwargs) {
    return PyUnicode_FromString(repo_author());
}

PyObject *_repo_email(PyObject *self, PyObject *args, PyObject *kwargs) {
    return PyUnicode_FromString(repo_email());
}

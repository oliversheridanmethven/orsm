#include <Python.h>
#include "suppressor.h"
#include "binding/wrappers.h"

PyObject *_suppressing_start(PyObject *self, PyObject *args, PyObject *kwargs) {
    suppressing_start();
    Py_RETURN_NONE;
}

PyObject *_suppressing_stop(PyObject *self, PyObject *args, PyObject *kwargs) {
    suppressing_stop();
    Py_RETURN_NONE;
}

static PyMethodDef suppressor_methods[] = {
        {"suppressing_start", PyFunc(_suppressing_start), METH_VARARGS | METH_KEYWORDS,
                                       "Start suppressing standard output."},
        {"suppressing_stop",  PyFunc(_suppressing_stop),  METH_VARARGS | METH_KEYWORDS,
                                       "stop suppressing standard output."},
        {NULL,                NULL, 0, NULL} /* Sentinel */
};

static struct PyModuleDef suppressor_module = {
        PyModuleDef_HEAD_INIT,
        "suppressor",
        "A simple module to suppress standard output in C extensions.",
        -1,
        suppressor_methods};

PyMODINIT_FUNC
PyInit_suppressor(void) {
    PyObject *module = PyModule_Create(&suppressor_module);
    if (!module) {
        fprintf(stderr, "Unable to create the suppressor module.");
        return nullptr;
    }

    return module;
}

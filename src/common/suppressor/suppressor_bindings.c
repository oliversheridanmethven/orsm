#include <Python.h>
#include "suppressor.h"
#include "binding/wrappers.h"

PyObject *suppressing_start_(PyObject *self, PyObject *args, PyObject *kwargs) {
    suppressing_start();
    Py_RETURN_NONE;
}

PyObject *suppressing_stop_(PyObject *self, PyObject *args, PyObject *kwargs) {
    suppressing_stop();
    Py_RETURN_NONE;
}

static PyMethodDef suppressor_methods[] = {
        {"suppressing_start", PyFunc(suppressing_start_), METH_VARARGS | METH_KEYWORDS,
                                       "Start suppressing standard output."},
        {"suppressing_stop",  PyFunc(suppressing_stop_),  METH_VARARGS | METH_KEYWORDS,
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
PyInit_suppressor_bindings(void) {
    PyObject *module = PyModule_Create(&suppressor_module);
    if (!module) {
        fprintf(stderr, "Unable to create the suppressor module.");
        return nullptr;
    }

    return module;
}

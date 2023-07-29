#include "examples_bindings.h"
#include "wrappers.h"

static PyMethodDef binding_methods[] = {
        {"hello_world",       PyFunc(_hello_world),       METH_VARARGS | METH_KEYWORDS,
                                       "Says hello world."},
        {"foo",               PyFunc(_foo),               METH_VARARGS | METH_KEYWORDS,
                                       "Prints an arg and kwarg argument."},
        {"fatal_failure",     PyFunc(_fatal_failure),     METH_VARARGS | METH_KEYWORDS,
                                       "Fails and calls exit()."},
        {"non_fatal_failure", PyFunc(_non_fatal_failure), METH_VARARGS | METH_KEYWORDS,
                                       "Fails in a way Python can catch."},
        {"set_at_exit",       PyFunc(_set_at_exit),       METH_VARARGS | METH_KEYWORDS,
                                       "Sets functionality to execute on exiting."},
        {NULL,                NULL, 0, NULL} /* Sentinel */
};

static struct PyModuleDef binding_module = {
        PyModuleDef_HEAD_INIT,
        "binding",
        "A simple module to demonstrate C bindings.",
        -1,
        binding_methods};

PyMODINIT_FUNC
PyInit_binding(void) {
    PyObject *module = PyModule_Create(&binding_module);
    if (!module) {
        fprintf(stderr, "Unable to create the binding module.");
        return nullptr;
    }

    return module;
}

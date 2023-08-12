#include "examples_bindings.h"
#include "binding/wrappers.h"

static PyMethodDef examples_methods[] = {
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

static struct PyModuleDef examples_module = {
        PyModuleDef_HEAD_INIT,
        "examples",
        "A simple module giving examples to demonstrate C bindings.",
        -1,
        examples_methods};

PyMODINIT_FUNC
PyInit_examples_bindings(void) {
    PyObject *module = PyModule_Create(&examples_module);
    if (!module) {
        fprintf(stderr, "Unable to create the examples module.");
        return nullptr;
    }

    return module;
}

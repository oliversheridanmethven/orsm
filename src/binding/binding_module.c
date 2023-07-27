#include "examples_bindings.h"

#define PyFunc(func)                                                                                     \
    /* An awkward cast necessary for functions of the form def foo(*args, **kwargs) */                   \
    /* https://docs.python.org/3/extending/extending.html#keyword-parameters-for-extension-functions/ */ \
    ((PyCFunction) (void (*)(void)) func)

static PyMethodDef binding_methods[] = {
        {"hello_world", PyFunc(_hello_world), METH_VARARGS | METH_KEYWORDS,
         "Says hello world."},
        {"foo", PyFunc(_foo), METH_VARARGS | METH_KEYWORDS,
         "Prints an arg and kwarg argument."},
        {"fail", PyFunc(_fail), METH_VARARGS | METH_KEYWORDS,
         "Fails and calls exit()."},
        {"set_at_exit", PyFunc(_set_at_exit), METH_VARARGS | METH_KEYWORDS,
         "Sets functionality to execute on exiting."},
        {NULL, NULL, 0, NULL} /* Sentinel */
};

static struct PyModuleDef binding_module = {
        PyModuleDef_HEAD_INIT,
        "binding",
        "A simple module to demonstrate C bindings.",
        -1,
        binding_methods};

PyMODINIT_FUNC
PyInit_binding(void)
{
    return PyModule_Create(&binding_module);
}

#include <Python.h>
#include <stdio.h>

static PyObject *hello_example(PyObject *self, PyObject *args)
{
    // Unpack a string from the arguments
    const char *strArg;
    if (!PyArg_ParseTuple(args, "s", &strArg))
        return NULL;

    // Print message and return None
    PySys_WriteStdout("Hello, %s!\n", strArg);
    Py_RETURN_NONE;
}

//-----------------------------------------------------------------------------
static PyMethodDef hello_methods[] = {
        {"hello",
         hello_example,
         METH_VARARGS,
         "Prints back 'Hello <param>', for example example: hello.hello('you')"},
        {NULL, NULL, 0, NULL} /* Sentinel */
};

//-----------------------------------------------------------------------------
static struct PyModuleDef hello_module_def = {
        PyModuleDef_HEAD_INIT,
        "hello",
        "Internal \"hello\" module",
        -1,
        hello_methods};

PyMODINIT_FUNC PyInit_hello(void)
{
    return PyModule_Create(&hello_module_def);
}

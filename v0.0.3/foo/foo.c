#include <Python.h>
#include <stdio.h>

static PyObject *foo_example(PyObject *self, PyObject *args)
{
    // Unpack a string from the arguments
    const char *strArg;
    if (!PyArg_ParseTuple(args, "s", &strArg))
        return NULL;

    // Print message and return None
    PySys_WriteStdout("foo, %s!\n", strArg);
    Py_RETURN_NONE;
}

//-----------------------------------------------------------------------------
static PyMethodDef foo_methods[] = {
        {"foo",
         foo_example,
         METH_VARARGS,
         "Prints back 'Bar <param>', for example example: hello.hello('you')"},
        {NULL, NULL, 0, NULL} /* Sentinel */
};

//-----------------------------------------------------------------------------
static struct PyModuleDef foo_module_def = {
        PyModuleDef_HEAD_INIT,
        "foo",
        "Internal \"foo\" module",
        -1,
        foo_methods};

PyMODINIT_FUNC PyInit_foo(void)
{
    return PyModule_Create(&foo_module_def);
}

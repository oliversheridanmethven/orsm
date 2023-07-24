#include <Python.h>
#include <stdio.h>

static PyObject *bar_example(PyObject *self, PyObject *args)
{
    // Unpack a string from the arguments
    const char *strArg;
    if (!PyArg_ParseTuple(args, "s", &strArg))
        return NULL;

    // Print message and return None
    PySys_WriteStdout("Bar, %s!\n", strArg);
    Py_RETURN_NONE;
}

//-----------------------------------------------------------------------------
static PyMethodDef bar_methods[] = {
        {"bar",
         bar_example,
         METH_VARARGS,
         "Prints back 'Bar <param>', for example example: hello.hello('you')"},
        {NULL, NULL, 0, NULL} /* Sentinel */
};

//-----------------------------------------------------------------------------
static struct PyModuleDef bar_module_def = {
        PyModuleDef_HEAD_INIT,
        "bar",
        "Internal \"bar\" module",
        -1,
        bar_methods};

PyMODINIT_FUNC PyInit_bar(void)
{
    return PyModule_Create(&bar_module_def);
}

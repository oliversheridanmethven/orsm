#include <Python.h>
#include <stdio.h>

static PyObject *fox_example(PyObject *self, PyObject *args)
{
    // Unpack a string from the arguments
    const char *strArg;
    if (!PyArg_ParseTuple(args, "s", &strArg))
        return NULL;

    // Print message and return None
    PySys_WriteStdout("fox, %s!\n", strArg);
    Py_RETURN_NONE;
}

//-----------------------------------------------------------------------------
static PyMethodDef fox_methods[] = {
        {"fox",
         fox_example,
         METH_VARARGS,
         "Prints back 'Bar <param>', for example example: hello.hello('you')"},
        {NULL, NULL, 0, NULL} /* Sentinel */
};

//-----------------------------------------------------------------------------
static struct PyModuleDef fox_module_def = {
        PyModuleDef_HEAD_INIT,
        "fox",
        "Internal \"fox\" module",
        -1,
        fox_methods};

PyMODINIT_FUNC PyInit_fox(void)
{
    return PyModule_Create(&fox_module_def);
}

#include <Python.h>
#include <stdio.h>

static PyObject *baz_example(PyObject *self, PyObject *args)
{
    // Unpack a string from the arguments
    const char *strArg;
    if (!PyArg_ParseTuple(args, "s", &strArg))
        return NULL;

    // Print message and return None
    PySys_WriteStdout("baz, %s!\n", strArg);
    Py_RETURN_NONE;
}

//-----------------------------------------------------------------------------
static PyMethodDef baz_methods[] = {
        {"baz",
         baz_example,
         METH_VARARGS,
         "Prints back 'baz <param>', for example example: hello.hello('you')"},
        {NULL, NULL, 0, NULL} /* Sentinel */
};

//-----------------------------------------------------------------------------
static struct PyModuleDef baz_module_def = {
        PyModuleDef_HEAD_INIT,
        "baz",
        "Internal \"baz\" module",
        -1,
        baz_methods};

PyMODINIT_FUNC PyInit_baz(void)
{
    return PyModule_Create(&baz_module_def);
}

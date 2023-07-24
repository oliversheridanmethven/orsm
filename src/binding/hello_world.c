#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

static PyObject *
_hello_world(PyObject *self, PyObject *args)
{
    const char *command;
    int rc;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    rc = puts("Hello world from within C.\n");
    if (rc == EOF || rc < 0)
    {
        return NULL;
    }
    return PyLong_FromLong(rc);
}

static PyMethodDef hello_world_methods[] = {
        {"hello_world", _hello_world, METH_VARARGS,
         "Execute a shell command."},
        {NULL, NULL, 0, NULL} /* Sentinel */
};

static struct PyModuleDef hello_world_module = {
        PyModuleDef_HEAD_INIT,
        "hello_world",                   /* name of module */
        "My simple hello_world module.", /* module documentation, may be NULL */
        -1,                              /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
        hello_world_methods};

PyMODINIT_FUNC
PyInit_hello_world(void)
{
    return PyModule_Create(&hello_world_module);
}

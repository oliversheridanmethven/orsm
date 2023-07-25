#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

void hello_world(void)
{
    int rc = puts("Hello world from within C.\n");
    if (rc == EOF || rc < 0)
    {
        exit(1);
    }
}

static PyObject *_hello_world(PyObject *self, PyObject *args, PyObject *kwargs)
{
    hello_world();
    Py_RETURN_NONE;
}

void func(int a, char *b)
{
    int rc = printf("The input values are: a = %i and b = %s\n", a, b);
    if (rc < 0)
    {
        exit(1);
    }
}

static PyObject *_func(PyObject *self, PyObject *args, PyObject *kwargs)
{
    /* This is the python equivalent of: def foo(a, b="default", **kwargs): ...  */
    static char *keywords[] = {"a", "b", NULL};
    //    PyObject *_a;
    /* Integers in Python are stored as a long, whereas in C I want an int. Hence we might need
     * to do some error checking or handling if we permit very long ints to be entered. */
    int a;
    char *b = "default";

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "i|s:_func", keywords, &a, &b))
    {
        /* The arguments passed don't correspond to the signature described. */
        return NULL;
    }
    //    a = PyLong_AsLong(_a);
    func(a, b);
    return PyLong_FromLong(a);
}


#define PyFunc(func)                                                                                     \
    /* An akward cast necessary for functions of the form def foo(*args, **kwargs) */                    \
    /* https://docs.python.org/3/extending/extending.html#keyword-parameters-for-extension-functions/ */ \
    ((PyCFunction) (void (*)(void)) func)

static PyMethodDef binding_methods[] = {
        {"hello_world", PyFunc(_hello_world), METH_VARARGS | METH_KEYWORDS,
         "Says hello world."},
        {"func", PyFunc(_func), METH_VARARGS | METH_KEYWORDS,
         "Prints an arg and kwarg argument."},
        {NULL, NULL, 0, NULL} /* Sentinel */
};

static struct PyModuleDef binding_module = {
        PyModuleDef_HEAD_INIT,
        "binding",                   /* name of module */
        "My simple binding module.", /* module documentation, may be NULL */
        -1,                          /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
        binding_methods};

PyMODINIT_FUNC
PyInit_binding(void)
{
    return PyModule_Create(&binding_module);
}

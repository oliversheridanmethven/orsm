#include "version_bindings.h"
#include "binding/wrappers.h"

static PyMethodDef version_methods[] = {
        {"repo_name",    PyFunc(_repo_name),    METH_VARARGS | METH_KEYWORDS,
                                  "The repository's name."},
        {"repo_version", PyFunc(_repo_version), METH_VARARGS | METH_KEYWORDS,
                                  "The repository's version."},
        {"repo_author",  PyFunc(_repo_author),  METH_VARARGS | METH_KEYWORDS,
                                  "The repository's author."},
        {"repo_email",   PyFunc(_repo_email),   METH_VARARGS | METH_KEYWORDS,
                                  "The repository's email."},
        {NULL,           NULL, 0, NULL} /* Sentinel */
};

static struct PyModuleDef version_module = {
        PyModuleDef_HEAD_INIT,
        "versions",
        "A simple module giving version information.",
        -1,
        version_methods};

PyMODINIT_FUNC
PyInit_version_bindings(void) {
    PyObject *module = PyModule_Create(&version_module);
    if (!module) {
        fprintf(stderr, "Unable to create the version module.");
        return nullptr;
    }

    return module;
}

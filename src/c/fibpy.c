#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "fib.c"

/* This function always takes two arguments */
/* self points to the object associated with the function */
/* args points to the Python tuple containing the arguments */
static PyObject *
spam_system(PyObject *self, PyObject *args)
{
    unsigned long *nth_fibonacci;

    // Convert Python tuple to C-type
    if (!PyArg_ParseTuple(args, "l", &nth_fibonacci))
        return NULL;

    return PyLong_FromLong(fib(nth_fibonacci));
}

static PyMethodDef SpamMethods[] = {
    {"system", spam_system, METH_VARARGS,
     "Execute a shell command."},
    {NULL, NULL, 0, NULL} /* Sentinel */
};

static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "fib_c", /* name of module */
    NULL,    /* module documentation, may be NULL */
    -1,      /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    SpamMethods};

PyMODINIT_FUNC
PyInit_fib_c(void)
{
    return PyModule_Create(&spammodule);
}
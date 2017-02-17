/*
 * _nativefileselect.c
 * 
 * Copyright 2017 notna <notna@apparat.org>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */

#include <Python.h>
#include <nfd.h>

static char _nativefileselect_doc[] =
    "Internal Module used for native file selection dialogues";

static PyObject *
_nativefileselect_openDialog(PyObject *self, PyObject *args)
{
    const char *filters_py;
    PyObject *result_py;
    
    if (!PyArg_ParseTuple(args, "s", &filters_py))
        return NULL;
    
    // Code here
    
    nfdchar_t *filters = (nfdchar_t*)filters_py;
    
    nfdchar_t *outPath = NULL;
    nfdresult_t result = NFD_OpenDialog( filters, NULL, &outPath );

    if ( result == NFD_OKAY ) {
        //puts("Success!");
        //puts(outPath);
        result_py = PyString_FromString(outPath);
        free(outPath);
        return result_py;
    }
    else if ( result == NFD_CANCEL ) {
        Py_RETURN_NONE;
    }
    else {
        //printf("Error: %s\n", NFD_GetError() );
        Py_RETURN_NONE;
    }

    return 0;
    
    Py_XDECREF(filters_py);
    Py_RETURN_NONE;
};


static PyMethodDef _NativefileselectMethods[] = {
    {"openDialog", (PyCFunction) _nativefileselect_openDialog, METH_VARARGS,
     "Opens a native dialog asking for a path"},
     
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef _nativefileselectmodule = {
    PyModuleDef_HEAD_INIT,
    "_nativefileselect",
    _nativefileselect_doc,
    -1,
    
    _NativefileselectMethods,
    NULL,NULL,NULL,NULL,
};

PyMODINIT_FUNC
PyInit__nativefileselect(void)
{
    PyModule_Create(&_nativefileselectmodule);
}

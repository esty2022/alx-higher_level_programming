// Entry point of the Python C API.
// C extensions should only #include <Python.h>, and not include directly
// the other Python header files included by <Python.h>.

#ifndef Py_PYTHON_H
#define Py_PYTHON_H

// Since this is a "meta-include" file, no #ifdef __cplusplus / extern "C" {

// Include Python header files
#include "patchlevel.h"
#include "pyconfig.h"
#include "pymacconfig.h"

#if defined(__sgi) && !defined(_SGI_MP_SOURCE)
#  define _SGI_MP_SOURCE
#endif

// stdlib.h, stdio.h, errno.h and string.h headers are not used by Python
// headers, but kept for backward compatibility. They are excluded from the
// limited C API of Python 3.11.
#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 < 0x030b0000
#  include <stdlib.h>
#  include <stdio.h>              // FILE*
#  include <errno.h>              // errno
#  include <string.h>             // memcpy()
#endif
#ifndef MS_WINDOWS
#  include <unistd.h>
#endif
#ifdef HAVE_STDDEF_H
#  include <stddef.h>             // size_t
#endif

#include <assert.h>               // assert()
#include <wchar.h>                // wchar_t


#endif /* !Py_PYTHON_H */

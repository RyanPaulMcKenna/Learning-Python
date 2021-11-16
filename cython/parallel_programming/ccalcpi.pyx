from cython.parallel import parallel, prange
cimport openmp
from libc.stdlib cimport malloc, free
import cython


def calcpi(int n):
    cdef double result = 0.0
    cdef int num_threads
    cdef int i,si

    with nogil,parallel(num_threads=6): # thread per iteration ran concurrently
        for i in prange(2, n*2, 2):
            si = 1 if ((i/2) % 2 == 1) else -1
            result += 4.0 * si / ( i * ( i + 1.0) * (i + 2.0))
    return result + 3


#https://cython.readthedocs.io/en/latest/src/userguide/parallelism.html?highlight=extra_compile_args
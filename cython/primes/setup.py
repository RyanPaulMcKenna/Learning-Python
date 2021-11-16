from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize(['primes.pyx','primes_python_compiled.py','primes_c_plus_plus.pyx'], annotate=True))
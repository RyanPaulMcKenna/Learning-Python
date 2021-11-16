from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules= cythonize('example.pyx'))

# run in terminal:
# python setup.py build_ext --inplace
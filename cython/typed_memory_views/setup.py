from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize(['memory_views.pyx'], annotate=True))
from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize(['random_noise.pyx'], annotate=True))
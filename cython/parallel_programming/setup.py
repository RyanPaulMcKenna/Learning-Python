from distutils.core import setup
from Cython.Build import cythonize 
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("ccalcpi",
            ["ccalcpi.pyx"],
            extra_compile_args=['/openmp'], #-03 -ffast-math -march=native on linux
            extra_link_args=['/openmp'] # -fopenmp on linux
            )
]

setup(
    name= 'Calc Pi',
    # cmdclass= {"build_ext": build_ext},
    ext_modules = cythonize(ext_modules)
)

#https://cython.readthedocs.io/en/latest/src/userguide/parallelism.html?highlight=extra_compile_args
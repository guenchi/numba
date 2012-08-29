from distutils.core import setup, Extension
import numpy

setup(
    name = "numbapro",
    author = "Continuum Analytics, Inc.",
    author_email = "support@continuum.io",
    url = "http://www.continuum.io",
    license = "Proprietary",
    description = "compile Python code",
    ext_modules = [Extension(name = "numbapro._internal",
                             sources = ["numbapro/_internal.c"],
                             include_dirs = [numpy.get_include()])],
    packages = ['numbapro', 'llvm_cbuilder', 'numbapro.vectorize',
                'numbapro.tests',
                'numbapro.tests.basic_vectorize',
                'numbapro.tests.llvm_cbuilder',
                'numbapro.tests.parallel_vectorize',
                'numbapro.tests.stream_vectorize'],
    version = "0.5"
)

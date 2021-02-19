#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages, Extension
from setuptools_rust import Binding, RustExtension

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = []

setup_requirements = []

test_requirements = []

setup(
    author="Benjamin Bolbrinker",
    author_email='benjamin.bolbrinker@kemi.uu.se',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Interface Python with Fortran, Rust and C",
    install_requires=requirements,
    license="GNU General Public License v3",
    include_package_data=True,
    name='how-to-speedup-python',
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/benjaminbolbrinker/unitcellsampling',
    version='0.1.0',
    zip_safe=False,
    ext_modules=[Extension('fib_c', sources=['src/c/fibpy.c'])],
    rust_extensions=[RustExtension(
        "fib_rs", path="src/rust/Cargo.toml", binding=Binding.PyO3)]
)

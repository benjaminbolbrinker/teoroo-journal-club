#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages, Extension
from setuptools_rust import Binding, RustExtension

setup(
    author="Benjamin Bolbrinker",
    author_email='benjamin.bolbrinker@kemi.uu.se',
    python_requires='>=3.5',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Interface Python with Rust and C",
    license="GNU General Public License v3",
    include_package_data=True,
    name='uu-journal-club',
    url='https://github.com/benjaminbolbrinker/uu-journal-club.git',
    version='0.1.0',
    zip_safe=False,
    ext_modules=[Extension('fib_c',
                           sources=['src/c/fibpy.c'],
                           )
                ],
    rust_extensions=[RustExtension('fib_rs',
                                   path='src/rust/Cargo.toml',
                                   binding=Binding.PyO3,
                                   )
                    ]
)

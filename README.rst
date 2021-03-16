.. role:: bash(code)
   :language: bash

.. contents:: Table of contents
    :depth: 3

Description
###########

This is a simple Python project illustrating how Python functions can be exposed from both C and Rust 
using the C Python API (https://docs.python.org/3/extending/extending.html) 
and Rust's PyO3 crate (https://github.com/PyO3/pyo3), respectively.
The project is intended as a template and starting point for future projects. 

The project also contains a small (non-representative) benchmark of C, C++, Fortran, Rust, and Python to provide a feeling for the relative efficiency of these programming languages.

What is going on?
*****************

Inside the :code:`src/python` folder
------------------------------------

Let's assume we want to calculate the *n* th number of the Fibonacci sequence.
The following recursive function does the job.

.. code:: python

    def fib(n):
        if n <= 1:
            return 1
        return fib(n - 1) + fib(n - 2)

Arguably, this implementation is not the most efficient and has a time complexity of :math:`O(2^N)`.
E.g. calculating the 40th number requires :math:`2^{40}` recursive descents and a summation of :math:`2^{40} - 1` terms.
Using an interpreted language like Python this can take quite some time.

In reality, it would probably be better to improve the algorithm to increase computational efficiency, but in the following, we are trying to speed up this toy example using lower-level languages (C and Rust) instead.  

Inside the :code:`src/c` folder
-----------------

Two files are present here. The :code:`fib.c` file contains a C function which is equivalent to the code above.
We expose this function using the C Python API. This is done in the :code:`fibpy.c` file (for details refer to https://docs.python.org/3/extending/extending.html).

Inside the :code:`src/rust` folder
-----------------

When we want to expose Rust functions to Python using the PyO3 crate it is necessary to create a project using :code:`cargo`.
Similar to above, two files are present in the :code:`src` folder. The :code:`fib.rs` contains the Rust implementation of the Fibonacci function.
The :code:`lib.rs` exposes this function to Python (https://github.com/PyO3/pyo3).

The :code:`setup.py` file
-----------------

When we write code we usually want that it can be used and maintained by others.
In Python, the :code:`setup.py` allows us to install and distribute the package via something like :code:`pip install .`.

It seems obvious that our C or Rust code should be part of the package which we want to distribute.
When using python one usually distinguishes between built distributions and source distributions.
Built distributions can be thought of as binaries (although they might as well not be because they might only contain Python code) in which a package is compiled for particular hardware and operating system.
It is not feasible however to provide build distributions for every platform. 
Packagers solve this issue by turning source distributions into built distributions "on the fly".

Luckily, when using the Python C API or the PyO3 crate in combination with :code:`setuptools` we do not have to care about all that to much in detail.

When using the Python C API one can include the following parameter into the :code:`setup` function. 
This takes care of the compilation and linking process when installing the package using e.g. :code:`pip install .`.
Of course, the necessary compilers and dependencies have to be installed on the system for the compilation to succeed.

.. code:: python

    setup(
        ...,
        ext_modules=[Extension('fib_c',
                            sources=['src/c/fibpy.c'],
                            include_dirs=['src/c/include'],
                            )
                    ]
        ...
    )



Similarly, when using PyO3 one can include the following parameter. 

.. code:: python

    setup(
        ...,
        rust_extensions=[RustExtension('fib_rs',
                                    path='src/rust/Cargo.toml',
                                    binding=Binding.PyO3,
                                    )
                        ]
        ...
    )

More details on the PyO3 cate can be found here (https://github.com/PyO3/setuptools-rust).

The :code:`run.py` file
-----------------------

Now, after we have built and installed the source distribution one can import the function from the exposed module.
The respective functions are called and the result is directed to the standard output.


Benchmarks
----------

This project also includes a small benchmark on the Fibonacci implementation described above.implementation described above to provide a feeling for the performance of Rust compared with C, C++, Fortran, and Python.

Run the project
###############

Option 1: Docker (recommended, plattform independent)
******************************

Be sure to have docker installed on your system (https://docs.docker.com/get-docker/).

Build the docker image:

.. code:: bash

    docker build -t teoroo-journal-club .

Run the docker image:

.. code:: bash

    docker run teoroo-journal-club


Option 2: Pipenv (Ubuntu only)
******************************

Installation is tested on Ubuntu 20.04.

Prerequisites
------------

Make sure python (version => 3.5) is installed.
Also install: 
:code:`gcc`, :code:`g++`, :code:`gfortran`, :code:`rust`, :code:`python3-dev` and :code:`python-dev`

Run
---

Change your directory

.. code:: bash

    cd app/

Create a virtual environment

.. code:: bash

    pipenv shell

Install the package

.. code:: bash

    pipenv install .

For running the benchmarks type

.. code:: bash

    ./benchmark.sh

For running the interface script execute

.. code:: bash

    python run.py


Option 3: Pip (Ubuntu only)
***************************

Installation is tested on Ubuntu 20.04.

Prerequisites
------------

Make sure python (version => 3.5) is installed.
Also install: 
:code:`gcc`, :code:`g++`, :code:`gfortran`, :code:`rust`, :code:`python3-dev` and :code:`python-dev`

Run
---

Make sure python (version => 3.5) is installed.
Change your directory

.. code:: bash

    cd app/

Create a virtual environment

.. code:: bash

    pip3 shell

Install the package

.. code:: bash

    pip3 install . --user

For running the benchmarks type

.. code:: bash

    ./benchmark.sh

For running the interface script execute

.. code:: bash

    python3 run.py



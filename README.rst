.. role:: bash(code)
   :language: bash

.. contents:: Table of Contents
    :depth: 3

Description
###########

This is a simple Python project illustrating how Python functions can be exposed from both C and Rust 
using the C Python API (https://docs.python.org/3/extending/extending.html) 
and Rust's PyO3 library (https://github.com/PyO3/pyo3), respectively.

What is going on?
*****************

Inside the :code:`src/python` folder
------------------------------------

Let's assume we want to calculate the *n* th number of the Fibonacci sequence.
We have written the following recursive function.

.. code:: python

    def fib(n):
        if n <= 1:
            return 1
        return fib(n - 1) + fib(n - 2)

Arguably, this implementation is not the most efficient and has a time complexity of :math:`O(2^N)`.
E.g. calculating the 46th number requires :math:`2^{46}` recursive descents and :math:`2^{46} - 1` additions.
On a interpreted language like Python this can take quite some time.

In reality it would probably be better to improve the algorithm, but in the following we are trying to speed up this toy example using lower level languages instead.  

Inside the :code:`src/c` folder
-----------------

Two files are present here. The :code:`fib.c` file contains a C function which is equivalent to the code above.
We expose this function using the C Python API. This is done in the :code:`fibpy.c` file.

Inside the :code:`src/rust` folder
-----------------

When we want to expose Rust functions to Python using the PyO3 crate it is necessary to create a project using :code:`cargo`.
Similar to above, two files are present in the :code:`src` folder. The :code:`fib.rs` contains the Rust implementation of the Fibonacci function.
The :code:`lib.rs` exposes this function to Python.

The :code:`setup.py` file
-----------------

When we write code we usually want that it can be used and maintained by others.
In Python the :code:`setup.py` allows to us to install and distribute the package via somthing like :code:`pip install .`.

It seems obvious that the C or Rust codes that we have written should be part of the package which we want to distribute.

Describe Source and build distros.

Luckily, when using the Python C API or the PyO3 crate :code:`setuptools` we do not have to care about much of that.

When using the former include 

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



it is possible to 

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


The :code:`run.py` file
-----------------


Run the project
###############

Option 1: Docker (recommended)
******************************

Be sure docker is installed.

.. code:: bash

    sudo apt install docker.io

Build the docker image:

.. code:: bash

    docker build -t teoroo-journal-club .

Run the docker image:

.. code:: bash

    docker run teoroo-journal-club


Option 2: Pipenv 
****************

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


Option 3: Pip 
****************

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



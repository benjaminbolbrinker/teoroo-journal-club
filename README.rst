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

The project also contains a small (non-representative) benchmark of C, C++, Fortran, Rust and Python in order to provide a feeling for the effiency.

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
E.g. calculating the 46th number requires :math:`2^{46}` recursive descents and a summation of :math:`2^{46} - 1` terms.
Using an interpreted language like Python this can take quite some time.

In reality it would probably be better to improve the algorithm in order to increase computational efficiency, but in the following we are trying to speed up this toy example using lower level languages instead.  

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
In Python the :code:`setup.py` allows to us to install and distribute the package via somthing like :code:`pip install .`.

It seems obvious that the C or Rust codes that we have written should be part of the package which we want to distribute.
When using python one usually distinguishes between built distributions and source distribtions.
Built distribtions can be though of as binaries (although they might as well not be because they might only contain Python code) in which a package is compiled for a particular hardware and operating system.
It is not feasable however to provide build distributions for every platform. 
Packagers solve this issue by turning source distribtions into built distribtions "on the fly".

Luckily, when using the Python C API or the PyO3 crate in combination with :code:`setuptools` we do not have to care about all that to much in detail.

When using the Python C API one can include the following parameter into the :code:`setup` function. 
This takes care of the whole compilation and linking process when installing the package using e.g. :code:`pip install .`.

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

Now, after we have built and installed the source distribtion one can import the function from the exposed module.
The respective functions are called and the result is directed to the standart output.


Benchmarks
----------

This project also includes a small benchmark on the Fibonacci implementation described above.implementation described above in order to provide a feeling for the performance of Rust compared with C, C++, Fortran and Python.

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



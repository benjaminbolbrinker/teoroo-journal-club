Run the project
---------------

.. role:: bash(code)
   :language: bash


Option 1: Docker (recommended)
------------------------------

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
-----------------

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
-------------

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

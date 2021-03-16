Run the project
---------------

Option 1: Docker (recommended)
------------------------------

Be sure docker is installed.

.. code:: bash

    sudo apt install docker.io

Build the docker image:

`docker build -t teoroo-journal-club .`

Run the docker image:

`docker run teoroo-journal-club`


Option 2: Pipenv 
-----------------

Prerequisites
------------

Make sure python (version => 3.5) is installed.
Also install: 
`gcc`, `g++`, `gfortran`, `rust`, `python3-dev` and `python-dev`

Run
---

Change your directory

`cd app/`

Create a virtual environment

`pipenv shell`

Install the package

`pipenv install .`

For running the benchmarks type

`./benchmark.sh`

For running the interface script execute

`python run.py`


Option 3: Pip 
-------------

Prerequisites
------------

Make sure python (version => 3.5) is installed.
Also install: 
`gcc`, `g++`, `gfortran`, `rust`, `python3-dev` and `python-dev`

Run
---

Make sure python (version => 3.5) is installed.
Change your directory

`cd app/`

Create a virtual environment

`pip3 shell`

Install the package

`pip3 install . --user`

For running the benchmarks type

`./benchmark.sh`

For running the interface script execute

`python3 run.py`

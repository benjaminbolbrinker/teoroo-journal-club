FROM ubuntu:20.04

# Update
RUN apt-get update
RUN apt-get install -y apt-utils curl

# Get compilers
RUN apt-get install -y gcc g++ gfortran

RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Get python dependencies
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-pip

# Setup
COPY ./app /app
RUN pip3 install /app

WORKDIR /app 

# Run
CMD python3 -u ./run.py
CMD bash ./benchmark.sh


#!/usr/bin/bash

mkdir ./build -p
gfortran -fno-inline-small-functions -O3 -o ./build/fib_f03 ./src/fib.f03
gcc -fno-inline-small-functions -O3 -o ./build/fib_c ./src/fib.c
g++ -fno-inline-small-functions -O3 -o ./build/fib_cpp ./src/fib.cpp
rustc -C opt-level=3 -o ./build/fib_rs ./src/fib.rs 

echo "gfortran:"
time ./build/fib_f03
echo "-------------"
echo ""
echo "gcc:"
time ./build/fib_c
echo "-------------"
echo ""
echo "g++:"
time ./build/fib_cpp
echo "-------------"
echo ""
echo "rustc:"
time ./build/fib_rs
echo "-------------"
echo ""
echo "python:"
time python ./src/fib.py
echo "-------------"
echo ""
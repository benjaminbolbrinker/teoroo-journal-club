#!/usr/bin/bash

echo "#######################"
echo "#######################"
echo ""
echo "Running the benchmark"
echo ""

mkdir ./build -p
gfortran -fno-inline-small-functions -O3 -o ./build/fib_f03 ./src/fortran/fib.f03
gcc -fno-inline-small-functions -O3 -o ./build/fib_c ./src/c/fib.c
g++ -fno-inline-small-functions -O3 -o ./build/fib_cpp ./src/cpp/fib.cpp
rustc -C opt-level=3 -o ./build/fib_rs ./src/rust/src/fib.rs 

echo "gfortran:"
time ./build/fib_f03
echo "-------------"
echo ""
sleep 1
echo "gcc:"
time ./build/fib_c
echo "-------------"
echo ""
sleep 1
echo "g++:"
time ./build/fib_cpp
echo "-------------"
echo ""
sleep 1
echo "rustc:"
time ./build/fib_rs
echo "-------------"
echo ""
sleep 1
echo "python:"
time python3 ./src/python/fib.py
echo "-------------"
echo ""

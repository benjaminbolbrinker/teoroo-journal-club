#!/usr/bin/env python

import fib_c 
import fib_rs
import src.python.fib as fib_py

import time

start = time.time()
print("gcc says the 46th Fibonacci number is", fib_c.fib(46))
end = time.time()
print("in {:.3f} seconds".format(end - start))
print()

start = time.time()
print("rust says the 46th Fibonacci number is", fib_rs.fib(46))
end = time.time()
print("in {:.3f} seconds".format(end - start))
print()

start = time.time()
print("python says the 46th Fibonacci number is", fib_py.fib(46))
end = time.time()
print("in {:.3f} seconds".format(end - start))

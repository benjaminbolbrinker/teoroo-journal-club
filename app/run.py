#!/usr/bin/env python

import fib_c 
import fib_rs
import src.python.fib as fib_py

# Call C function
print("gcc says the 46th Fibonacci number is", fib_c.fib(46))
print()

# Call Rust function
print("rust says the 46th Fibonacci number is", fib_rs.fib(46))
print()

# Call Python function
print("python says the 46th Fibonacci number is", fib_py.fib(46))

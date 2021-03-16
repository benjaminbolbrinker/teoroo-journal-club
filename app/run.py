#!/usr/bin/env python

import fib_c 
import fib_rs

print("Calling foreign functions from python:")
print()

# Call C function
print("gcc says the 40th Fibonacci number is... ", end='')
print(fib_c.fib(40))
print()

# Call Rust function
print("rust says the 40th Fibonacci number is... ", end='')
print(fib_rs.fib(40))
print()

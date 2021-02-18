def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print("Python says the 46th Fibonacci number is ", fib(46))

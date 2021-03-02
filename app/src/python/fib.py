import tryout

def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    tryout.try_one(lambda: print("python says the 46th Fibonacci number is ", fib(46)), 15)

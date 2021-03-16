def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    print("python says the 40th Fibonacci number is ", fib(40))

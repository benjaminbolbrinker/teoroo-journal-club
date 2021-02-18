#include <cstdio>
#include <cstdint>

static uint64_t fib(uint64_t n)
{
    if (n <= 1)
        return 1;
    return fib(n - 1) + fib(n - 2);
}

int main()
{
    printf("g++ says the 46th Fibonacci number is %lu \n", fib(46));
    return 0;
}

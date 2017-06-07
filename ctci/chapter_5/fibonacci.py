"""
Write a method to generate the nth Fibonacci number.
"""


def fib_rec(n):
    if n <= 2:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)


def fib_it(n):
    if n == 0:
        return 0

    a = 1
    b = 1

    for i in range(3, n+1):
        c = a + b
        a = b
        b = c

    return b


if __name__ == '__main__':
    print(fib_rec(1))
    print(fib_rec(2))
    print(fib_rec(3))
    print(fib_rec(4))
    print(fib_rec(5))
    print(fib_rec(8))

    print(fib_it(1))
    print(fib_it(2))
    print(fib_it(3))
    print(fib_it(4))
    print(fib_it(5))
    print(fib_it(8))

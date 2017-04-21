"""
A natural number is called a prime if it is bigger than 1 and has no divisors other than 1 and itself.
Write a program that takes an integer argument and returns all the primes between 1 and that integer.
For example,if the input is 18,you should return (2,3,5,7,11,13,17).

The sieve of Eratosthenes, one of a number of prime number sieves, is a simple,
ancient algorithm for finding all prime numbers up to any given limit.
It does so by iteratively marking as composite (i.e., not prime)
the multiples of each prime, starting with the multiples of 2.
"""

import math


def primes(n):
    multiples = []
    primes = []

    for i in range(2, n+1):
        if i not in multiples:
            primes.append(i)

            for j in range(i*i, n+1, i):
                multiples.append(j)

    return primes


if __name__ == '__main__':
    print(primes(18))

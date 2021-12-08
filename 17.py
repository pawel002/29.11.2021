# primes that can be constructed by slicing 2 numbers

from sympy import *


def primeSlices(a, b, number, step):
    if a == 0 and b == 0:
        if isprime(number):
            return 1
        return 0
    if a == 0 and b > 0:
        return primeSlices(0, 0, b * (10 ** step) + number, step + 1)
    if b == 0 and a > 0:
        return primeSlices(0, 0, a * (10 ** step) + number, step + 1)
    else:
        return primeSlices(a//10, b, number + (a % 10) * (10 ** step), step + 1) +\
               primeSlices(a, b//10, number + (b % 10) * (10 ** step), step + 1)

print(primeSlices(1, 3, 0, 0))

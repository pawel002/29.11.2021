# Primes in binary
from math import sqrt


def is_prime(n):
    if 2 <= n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n <= 1:
        return False
    for i in range(6, int(sqrt(n) + 1), 6):
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False
    return True


def primeSlices(T, pos):
    if pos == len(T):
        return True
    for i in range(30):
        if pos + i < len(T):
            number = 0
            for j in range(i+1):
                if pos + j < len(T):
                    number += 2 ** (i-j) * T[pos + j]
            if is_prime(number):
                if primeSlices(T, pos + i + 1):
                    return True
    return False


T = [1, 1, 1, 0, 1, 1]
if primeSlices(T, 0):
    print("tak")
else:
    print("nie")




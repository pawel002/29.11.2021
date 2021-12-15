# sum of products of every subset of set containing distinct prime divisors

def factor(n):
    factors = []
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n //= 2
    if n % 3 == 0:
        factors.append(3)
        while n % 3 == 0:
            n //= 3
    i = 6
    while i * i <= 2 * n:
        if n % (i - 1) == 0:
            factors.append(i - 1)
            while n % (i - 1) == 0:
                n //= i - 1
        if n % (i + 1) == 0:
            factors.append(i + 1)
            while n % (i + 1) == 0:
                n //= i + 1
        i += 6
    if n > 2:
        factors.append(n)
    return factors


def recursive(arr, idx, curr_prod):
    if idx == len(arr):
        return 0
    return curr_prod * arr[idx] + recursive(arr, idx + 1, curr_prod * arr[idx]) + recursive(arr, idx + 1, curr_prod)


def factor_product(n):
    factors = factor(n)
    return recursive(factors, 0, 1)


print(factor_product(60))




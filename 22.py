def prime_factors(x):
    factors = []
    i = 2
    while i*i <= x:
        if x % i == 0:
            factors.append(i)
            while x % i == 0:
                x //= i
        i += 1
    if x >= 2:
        factors.append(x)
    return factors


def jump(T, idx):
    if idx == len(T) - 1:
        return True
    for x in prime_factors(T[idx]):
        if x != T[idx]:
            if jump(T, idx + x):
                return True
    return False


T = [9, 0, 4, 0, 4, 4]
print(jump(T, 0))

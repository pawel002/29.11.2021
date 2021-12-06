def is_prime(x):
    if 2 <= x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 6
    while i * i <= x:
        if x % (i - 1) == 0 or x % (i + 1) == 0:
            return False
        i += 6
    return True


def int_length(x):
    i = 0
    while 10 ** i <= x:
        i += 1
    return i


def delete_digit(x, i):
    L = int_length(x)
    x = (x % 10 ** (L - 1 - i)) + (x // (10 ** (L - i))) * (10 ** (L - i - 1))
    return x


def f(k, A):
    L = int_length(k)
    if L >= 2 and is_prime(k) and k not in A:
        print(k)
        A.append(k)
    for i in range(L):
        f(delete_digit(k, i), A)


A = []
f(43124, A)

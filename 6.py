# given T[n] find size of smallest subset with sum = sum of indexes

from random import randint


def f(T, S, ndx_sum):
    if S == ndx_sum:
        return True
    for i in range(len(T) - 1):
        if T[i] >= 0:
            T[i] *= -1
            next_S = S + T[i]
            next_ndx_sum = ndx_sum + i
            if f(T, next_S, next_ndx_sum):
                return True
    return False


N = 10
A = [randint(1, 10) for _ in range(N)]
print(*A)
f(A, 0, 0)

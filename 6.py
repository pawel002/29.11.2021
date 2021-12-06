# given T[n] find size of smallest subset with sum = sum of indexes

from random import randint


def f(T, S, ndx_sum, step):
    for i in range(len(T)):
        if T[i] >= 0:
            next_S = T[i] + S
            next_ndx_sum = ndx_sum + i
            if next_S == next_ndx_sum:
                print(next_S, step)
                return True
    for i in range(len(T)):
        if T[i] >= 0:
            next_S = T[i] + S
            next_ndx_sum = ndx_sum + i
            T[i] *= -1
            if f(T, next_S, next_ndx_sum, step + 1):
                return True
            T[i] *= -1
    return False


N = 10
A = [5, 10, 20, 30, 99, 0]
print(*A)
if not f(A, 0, 0, 1):
    print("NIE")

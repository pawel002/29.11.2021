# Determinant of a matrix
from random import randint
import numpy as np

def arr_print(T):
    for row in T:
        print(*row)


def arr_del(T, i, j):
    L = len(T)
    assert 0 <= i < L and 0 <= j < L, "Invalid input"
    T_new = [[0 for _ in range(L-1)] for _ in range(L-1)]
    for row in range(L - 1):
        for col in range(L - 1):
            if row >= i and col >= j:
                T_new[row][col] = T[row + 1][col + 1]
            elif row >= i:
                T_new[row][col] = T[row + 1][col]
            elif col >= j:
                T_new[row][col] = T[row][col + 1]
            else:
                T_new[row][col] = T[row][col]
    return T_new


def DET(T):
    L = len(T)
    if L == 1:
        return T[0][0]
    val = 0
    for j in range(L):
        for i in range(L):
            val += (-1) ** (i + j) * T[i][j] * DET(arr_del(T, i, j))
    return val


T = [[randint(1, 10) for i in range(3)] for j in range(3)]
a = np.array(T)
print(np.linalg.det(a))
arr_print(T)
print(DET(T)/6)

# 13 separable squares with collective area of 2012
# Probably not working
import copy


def colliding(sq1: tuple, sq2: tuple):
    if sq1[1] < sq2[0] or sq2[1] < sq1[0]:
        if sq1[3] < sq2[2] or sq2[2] < sq1[3]:
            return True
    return False


def square_area(sq):
    return (sq[1] - sq[0]) ** 2


def square_f(sq_arr):
    T = [None] * 13
    if recursive(sq_arr, T, 0, 0, 0):
        return True
    return False


def recursive(sq_arr, T, area, idx_sq_arr, idx_T):
    if area == 2012:
        return True
    if idx_T == 13:
        return False
    flag = True
    for sq in T:
        if colliding(sq, sq_arr[idx_sq_arr]):
            flag = False
    if flag:
        if recursive(sq_arr, T, area, idx_sq_arr + 1, idx_T):
            return True
    T_new = copy.deepcopy(T)
    T[idx_T] = sq_arr[idx_sq_arr]
    if recursive(sq_arr, T_new, area + square_area(sq_arr[idx_sq_arr]), idx_sq_arr + 1, idx_T + 1) or \
            recursive(sq_arr, T, area, idx_sq_arr + 1, idx_T):
        return True
    return False



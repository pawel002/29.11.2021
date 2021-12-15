def linear(a, b):
    return a + b


def parallel(a, b):
    return a*b/(a+b)


def RES(T, R):
    return resistor(T, 0, 0, R, 0) or resistor(T[::-1], 0, 0, R, 0)


def resistor(T, idx, res, S, num):
    if res == S:
        return True
    if num == 3 or idx >= len(T):
        return False
    A = resistor(T, idx + 1, res, S, num)
    B = resistor(T, idx + 1, linear(res, T[idx]), S, num + 1)
    C = resistor(T, idx + 1, parallel(res, T[idx]), S, num + 1)
    return A or B or C


T = [1, 4, 10]
print(RES(T, 50/15))




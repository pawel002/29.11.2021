import random


def min_king(T, k, pos, curr_price, max_price, step):
    if step == 0:
        curr_price = T[0][k]
    else:
        curr_price += T[pos[0]][pos[1]]
    if pos[1] == 7:
        max_price = max(max_price, curr_price)
    dir = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    for i in dir:
        if 0 <= pos[0] + i[0] < 8 and 0 <= pos[1] + i[1] < 8:
            min_king(T, k, [pos[0] + i[0], pos[1] + i[1]], max_price,)
    return max_price


T = [[random.randint(1, 100) for _ in range(8)] for _ in range(8)]
for row in T:
    print(*row)
print(min_king(T, 1, [0, 1], 0, 999999, 0))

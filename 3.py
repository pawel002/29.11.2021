from random import randint


def min_king(T, pos, depth):
    if pos[0] == 7 and pos[1] == 7:
        return T[pos[0]][pos[1]]
    if pos[0] > 7 or pos[1] > 7:
        return 0
    directions = [(1, -1), (1, 0), (1, 1)]
    Val = [0, 0, 0]
    for i in range(len(directions)):
        next_pos = [pos[0] + directions[i][0], pos[1] + directions[i][1]]
        Val[i] = min_king(T, next_pos, depth)
    if depth[pos[0]][pos[1]] == -1:
        depth[pos[0]][pos[1]] = T[pos[0]][pos[1]] + min(Val)
    return depth[pos[0]][pos[1]]


A = [[randint(1, 1000) for a in range(8)] for b in range(8)]
dp = [[-1 for _ in range(8)] for _ in range(8)]
k = 2
print(min_king(A, [0, k], dp))
for row in A:
    print(*row)
print()
for row in dp:
    print(*row)

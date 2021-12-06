# Knight board

def arr_print(T):
    for row in T:
        print(*row)


def knight(N, start_pos):
    T = [[0 for _ in range(N)] for _ in range(N)]
    if knight_step(T, start_pos, step=1, L=N):
        print("TAK")
        arr_print(T)
    else:
        print("NIE")


def knight_step(T, pos, step, L):
    T[pos[0]][pos[1]] = step
    if step == L*L:
        return True
    directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
    flag = True
    for leap in directions:
        next_pos = [pos[0] + leap[0], pos[1] + leap[1]]
        if 0 <= next_pos[0] < L and 0 <= next_pos[1] < L and T[next_pos[0]][next_pos[1]] == 0:
            if knight_step(T, next_pos, step + 1, L):
                flag = False
                return True
    if flag:
        T[pos[0]][pos[1]] = 0
    return False


knight(6, [0, 0])


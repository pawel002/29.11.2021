# Knight board
# NOT FINISHED

def arr_print(T):
    for row in T:
        print(*row)


def next_pos(T, pos, L):
    directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
    final_n_pos = [0, 0]
    least_free = 9
    flag = True
    for D in directions:
        n_pos = [pos[0] + D[0], pos[1] + D[1]]
        if 0 <= n_pos[0] < L and 0 <= n_pos[1] < L and T[n_pos[0]][n_pos[1]] == 0:
            flag = False
            curr_free = check_free(T, n_pos, L)
            if curr_free < least_free:
                final_n_pos = [n_pos[1], n_pos[1]]
                least_free = curr_free
    if flag:
        return False
    return final_n_pos


def check_free(T, pos, L):
    count = 0
    directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
    for D in directions:
        n_pos = [pos[0] + D[0], pos[1] + D[1]]
        if 0 <= n_pos[0] < L and 0 <= n_pos[1] < L and T[n_pos[0]][n_pos[1]] == 0:
            count += 1
    return count


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
    res = next_pos(T, pos, L)
    if res:
        if knight_step(T, res, step + 1, L):
            return True
    T[pos[0]][pos[1]] = 0
    return False


knight(7, [0, 0])
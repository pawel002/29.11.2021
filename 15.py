# 8 bishops problem
import copy


def arr_print(T):
    for row in T:
        print(*row)


def bishop_beat(T, pos, num):
    a1 = pos[1] - pos[0]
    a2 = pos[1] + pos[0]
    for x in range(8):
        if 0 <= x <= 7 and 0 <= x + a1 <= 7:
            T[x][x+a1] = num
        if 0 <= x <= 7 and 0 <= -x + a2 <= 7:
            T[x][-x+a2] = num


def bishop_place(T, num, possibleRows, possibleCols, chessBoars):
    if num == 9:
        global A
        if A == 1:
            chessBoars.append(T)
            arr_print(T)
            A += 1
    for row in possibleRows:
        for col in possibleCols:
            if T[row][col] == 0:
                T_new = copy.deepcopy(T)
                possibleR_new = copy.deepcopy(possibleRows)
                possibleR_new.remove(row)
                possibleC_new = copy.deepcopy(possibleCols)
                possibleC_new.remove(col)
                bishop_beat(T_new, [row, col], num)
                bishop_place(T_new,  num + 1, possibleR_new, possibleC_new, chessBoars)


def bishops():
    chessBoars = []
    T = [[0 for _ in range(8)] for _ in range(8)]
    possibleRows = [i for i in range(8)]
    possibleCols = [i for i in range(8)]
    bishop_place(T, 1, possibleRows, possibleCols, chessBoars)
    print(len(chessBoars))
    for chessBoard in chessBoars:
        arr_print(chessBoard)

A = 1
bishops()

# king + weird moves
# NO IDEA FOR Better_king

from random import randint
from math import sqrt
from termcolor import colored


def last_digit(n):
    return n % 10


def first_digit(n):
    if n >= 100000000:
        n //= 100000000
    if n >= 10000:
        n //= 10000
    if n >= 100:
        n //= 100
    if n >= 10:
        n //= 10
    return n


def angleCos(vec, tup):
    return (vec[0] * tup[0] + vec[1] * tup[1]) / sqrt((vec[0] ** 2 + vec[1] ** 2) * (tup[0] ** 2 + tup[1] ** 2))


def king_better(T, pos, end_pos, is_kings_turn, m_king, m_end):
    if pos == end_pos:
        T[pos[0]][pos[1]] *= -1
        return True
    directions = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]
    vec = [end_pos[0] - pos[0], end_pos[1] - pos[1]]
    directions.sort(key=lambda x: -angleCos(vec, x))
    for D in directions:
        next_pos = [pos[0] + D[0], pos[1] + D[1]]
        if 0 <= next_pos[0] <= 7 and 0 <= next_pos[1] <= 7 and T[next_pos[0]][next_pos[1]] > 0:
            if is_kings_turn:
                var = last_digit(T[pos[0]][pos[1]]) < first_digit(T[next_pos[0]][next_pos[1]])
            else:
                var = last_digit(T[next_pos[0]][next_pos[1]]) < first_digit(T[pos[0]][pos[1]])
            if var:
                T[pos[0]][pos[1]] *= -1
                if king_better(T, end_pos, next_pos, not is_kings_turn, m_king, m_end):
                    if is_kings_turn:
                        m_king.append(D)
                    else:
                        m_end.insert(0, (-D[0], -D[1]))
                    return True
                T[pos[0]][pos[1]] = abs(T[pos[0]][pos[1]])
    return False


T = [[randint(1, 100) for _ in range(8)] for _ in range(8)]
moves_king = []
moves_end = []
if king_better(T, [0, 0], [7, 7], True, moves_king, moves_end):
    for row in T:
        for ele in row:
            if ele < 0:
                print(colored(f"{ele : <5}", "red"), end="")
            else:
                print(f"{ele : <5}", end="")
        print()
    print(*moves_king, end=" ")
    print(*moves_end, end=" ")
else:
    print("NIE")


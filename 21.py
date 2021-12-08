# is there a subset with given sum in 2D arr


def subset(T, S):
    possibleRows = [i for i in range(1, len(T) + 1)]
    possibleCols = [i for i in range(1, len(T[0]) + 1)]
    for row in possibleCols:
        if row > 0:
            for col in possibleCols:
                if col > 0:
                    if T[row][col] < S:


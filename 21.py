# is there a subset with given sum in 2D arr


def subset(T, S, possibleRows, possibleCols):
    if S == 0:
        return True
    for row in possibleCols:
        if row > 0:
            for col in possibleCols:
                if col > 0:
                    if T[row - 1][col - 1] <= S and possibleRows[row - 1] > 0 and possibleCols[col - 1] > 0:
                        possibleRows[row - 1] *= -1
                        possibleCols[col - 1] *= -1
                        if subset(T, S - T[row - 1][col - 1], possibleRows, possibleCols):
                            print(T[row - 1][col - 1])
                            return True
                        possibleRows[row - 1] *= -1
                        possibleCols[col - 1] *= -1
    return False


def f(T, S):
    possibleRows = [i for i in range(1, len(T) + 1)]
    possibleCols = [i for i in range(1, len(T[0]) + 1)]
    return subset(T, S, possibleRows, possibleCols)


A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(f(A, 16))

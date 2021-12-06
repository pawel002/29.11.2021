# Subset Sum
def isSubsetSum(T: list, s, elements):
    if s == 0:
        return True
    if s < 0 or elements == 0:
        return False

    if T[elements - 1] > s:
        return isSubsetSum(T, s, elements - 1)

    return isSubsetSum(T, s, elements - 1) or isSubsetSum(T, s - T[elements - 1], elements - 1)


A = [3, 34, 4, 12, 5, 2]
L = len(A)
print(isSubsetSum(A, 21, L))



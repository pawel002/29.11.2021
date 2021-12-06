# Subset Summation/Subtraction
def isSubsetSum(T: list, s, elements):
    if s == 0:
        return True
    if s < 0 or elements == 0:
        return False

    if T[elements - 1] > s:
        return isSubsetSum(T, s, elements - 1) or isSubsetSum(T, s + T[elements - 1], elements - 1)

    return isSubsetSum(T, s, elements - 1) or isSubsetSum(T, s - T[elements - 1], elements - 1) or \
           isSubsetSum(T, s + T[elements - 1], elements - 1)


A = [1, 3, 7, 101]
L = len(A)
print(isSubsetSum(A, 92, L))



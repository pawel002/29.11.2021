# Subset Summation/Subtraction
def isSubsetSum(T: list, s, elements):
    if s == 0:
        return True
    if elements == 0:
        return False

    return isSubsetSum(T, s, elements - 1) or isSubsetSum(T, s - T[elements - 1], elements - 1) or \
           isSubsetSum(T, s + T[elements - 1], elements - 1)


A = [1, 3, 7, 101, 26]
L = len(A)
print(isSubsetSum(A, 22, L))



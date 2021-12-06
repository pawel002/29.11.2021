# Subset Summation/Subtraction
def isSubsetSum(T: list, s, elements):
    if s == 0:
        return True
    if s < 0 or elements == 0:
        return False

    A = isSubsetSum(T, s + T[elements - 1], elements - 1)
    B = isSubsetSum(T, s, elements - 1)
    C = isSubsetSum(T, s - T[elements - 1], elements - 1)

    if T[elements - 1] > s:
        A = isSubsetSum(T, s + T[elements - 1], elements - 1)
        B = isSubsetSum(T, s, elements - 1)
        if A:
            print("+" + str(T[elements - 1]), sep="")
        return A or B

    if A:
        print("-" + str(T[elements - 1]), sep="")
    return A or B or C


A = [1, 3, 7, 101]
L = len(A)
print(isSubsetSum(A, 92, L))
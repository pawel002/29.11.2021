# can you divide a set into 3 subsets with same numbers of 1 in binary representation

def ones_in_bin(x):
    count = 0
    while x:
        x &= x - 1
        count += 1
    return count


def bin_subset(T):
    A = [ones_in_bin(x) for x in T]
    return recursion(A, 0, 0, 0, 0)


def recursion(T, sum1, sum2, sum3, idx):
    if sum1 == sum2 == sum3 and sum1 != 0:
        return True
    if idx >= len(T):
        return False

    A = recursion(T, sum1 + T[idx], sum2, sum3, idx + 1)
    B = recursion(T, sum1, sum2 + T[idx], sum3, idx + 1)
    C = recursion(T, sum1, sum2, sum3 + T[idx], idx + 1)
    D = recursion(T, sum1, sum2, sum3, idx + 1)

    return A or B or C or D


arr = [2, 3, 5, 7, 15]
print(bin_subset(arr))

# some functions
# prime check
def is_prime(n):
    if 2 <= n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 6
    while i * i <= n:
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False
    return True


# number of ones in binary
def binary_ones(x):
    count = 0
    while x > 0:
        x &= x - 1
        count += 1
    return count


# conversion to any base
def dec_to_base(num, base):
    base_num = ""
    while num > 0:
        dig = int(num % base)
        if dig < 10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A') + dig - 10)
        num //= base
    return int(base_num[::-1])


# NWD
def NWD(a, b):
    while a:
        a, b = b % a, a
    return b


# NWW
def NWW(a, b):
    return int(a * b / NWD(a, b))


# comparing every two elements of 2D array
def compare(A):
    R = len(A)
    C = len(A[0])
    for i in range(R * C):
        row = i // C
        col = i % C
        for j in range(i, R * C):
            row_ = j // C
            col_ = j % C
            pass  # FUNCTION OF T[row][col] and T[row_][col_]


# sum in a row
def row_sum(Arr, row):
    sum = 0
    for x in Arr[row]:
        sum += x
    return sum


# sum in na column
def col_sum(Arr, col):
    sum = 0
    for i in range(len(Arr)):
        sum += Arr[i][col]
    return sum






print(NWD(25, 10))
print(NWW(25, 10))

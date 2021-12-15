# Ax1, Bx0, 1st bit = 1, how many composite numbers

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


def bin_to_dec(num):
    sum = 0
    for i in range(len(str(num))):
        sum += (2 ** i) * ((num // 10 ** i) % 10)
    return sum


# Assuming A > 1
def composite(A, B, num, step=0):
    if step == 0:
        num = 1
        A -= 1
    prime = is_prime(bin_to_dec(num))
    if A == 0 and B == 0 and not prime:
        return 1
    if A < 0 or B < 0:
        if prime:
            return 0
    if A > 0 and B > 0:
        return composite(A - 1, B, num * 10 + 1, step + 1) + composite(A, B - 1, num * 10, step + 1)
    if B > 0:
        return composite(A, B - 1, num*10, step + 1)
    return 0


print(composite(2, 3, 0))


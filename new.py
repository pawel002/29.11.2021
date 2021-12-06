def lol(n):
    print(n)
    if n == 0:
        return 6
    if n == 1:
        return 21
    else:
        return 2*(3 ** n) + 4*lol(n-1) - 3*lol(n-2)

N = 30
L = 3 + 3 * (3 ** N) + 3*N*(3 ** N)
print(L)
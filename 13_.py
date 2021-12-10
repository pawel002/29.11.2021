def partition(A):
    table = [[[1]]] + [None]*(A-1)
    for i in range(1, A):
        table[i] = [[i+1]]
        for k in range(i):
            table[i].extend([[i-k]+l for l in table[k] if i-k >= l[0]])
    return table[-1]


def print_partition(A):
    for i in reversed(partition(A)):
        print(*i)


print_partition(5)
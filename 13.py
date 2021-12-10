# Possible partitions

def arr_print(arr):
    for i in range(len(arr)):
        print(arr[i], end="")
        if i + 1 == len(arr) or arr[i + 1] == 0:
            break
        print("+", end="")
    print()


def partition(remVal, maxVAl, idx, count):
    if remVal == 0:
        arr_print(idx)



partition(8)






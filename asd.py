sum = 0
for i in range(50 + 1):
    sum_ = 1
    for j in range(i + 1):
        sum_ *= (100 - 2*j)
    sum += sum_
print(sum)




count = 0
for x in range(1100000000, 1987653211):
    if x%16 in [10,15] or x%8 in [0,3]:
        count += 1
print(count)
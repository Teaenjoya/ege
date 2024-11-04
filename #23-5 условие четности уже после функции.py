def f(st, en):
    if st > en:
        return 0
    if st == en:
        return 1
    if st < en:
        return f(st + 1, en) + f(st * 2, en) + f(st * 3, en)
res = 0
for st in range (2, 15):
    if st % 2 == 0:
        res += f(st, 15)
print (res)
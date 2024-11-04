def f(st, en):
    if st > en:
        return 0
    if st == en:
        return 1
    if st < en:
        return f(st + 2, en) + f(st + 4, en) + f(st + 5, en)
for en in range (32,100):
    if f(31, en) == 1001:
        print (en)
        break
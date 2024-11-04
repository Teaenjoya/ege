def f(st,en):
    if st < en or st in (9,16): #не проходит через 9 или 16
        return 0
    if st == en:
        return 1
    if st > en:
        return f(st - 1, en) + f(st - 2, en) + f(st // 3, en)
print(f(19,3))
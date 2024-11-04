def f(st, en):
    if st > en or st == 90: #не проходит через 90
        return 0
    if st == en:
        return 1
    if st < en:
        return f(st + 1, en) + f(st * 2, en) + f(st * 3, en)
print(f(3, 30)*f(30,100)*f(100,184)) #проходит через эти значения

def f(s, e):
    if s < e:
        return 0
    if s == e:
        return 1
    if s > e:
        return f(s - 4, e) + f(s - sum(map(int, str(s))), e)
print (f(36, 14) * f(14, 2))
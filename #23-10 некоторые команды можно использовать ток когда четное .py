def f(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    if s < e:
        res = 0
        if s % 2 == 0:
            res += f(s + 1, e) + f(s + 2, e)
        res += f(s * 2, e)
        return res
print (f(1, 32))
def f(s, e):
    if s > e or '5' in str(s):
        return 0
    if s == e:
        return 1
    if s < e:
        return f(s + 1, e) + f(s * 2, e)
print (f(1, 60))
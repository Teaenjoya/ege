c = set()
def f(s, e, c):
    if s > e or c > 6:
        return 0
    if s == e and c == 6:
        return 1
    if s < e or c < 6:
        return f(s + 1, e, c + 1) + f(s + 2, e, c + 1) + f(s * 2, e, c + 1)
for e in range (34,60):
    if f(1, e, 0) != 0:
        c.add(e)
print(len(c))

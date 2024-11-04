c = set()
for n in range (10,101):
    s = '3' + '7' * n
    while '27' in s or '377' in s or '777' in s:
            s = s.replace ('27', '32', 1)
            s = s.replace ('377', '27', 1)
            s = s.replace('777', '3', 1)
    if sum(map(int, s)) % 22 == 0:
        c.add(n)
print(max(c))
from functools import lru_cache
@lru_cache()
def f(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    elif n > 1 and n % 2 == 0:
        return f(n // 2) + 1
    elif n > 1 and n % 2 != 0:
        return f(n // 2)
for n in range (0, 10000):
    if f(n) == 10:
        print (n)
        break
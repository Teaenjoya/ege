from functools import lru_cache
@lru_cache()
def f(n):
    if n < 3:
        return 1
    elif n > 2:
        return f(n - 1) + f(n - 2)
for n in range (1, 1007):
    f(n)
print ((f(1006)-f(1004))/f(1005))
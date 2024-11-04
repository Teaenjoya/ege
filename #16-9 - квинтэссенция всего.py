from functools import lru_cache
@lru_cache()
def f(n):
    if n <= 1:
        return 1
    elif n > 1 and n % 2 == 0:
        return f(n - 1) - n
    else:
        return 11 * f(n - 2) + n
k = 0
for n in range (35, 51):
    if f(n) % 2 == 0:
        k += f(n)
print (len(str(k)))

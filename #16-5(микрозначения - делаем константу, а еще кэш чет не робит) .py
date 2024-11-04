from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 1025:
        return 1
    else:
        return f(n-1) * 3**(n % 5) / 3**(n % 7)
print (f(1025)/f(1030))
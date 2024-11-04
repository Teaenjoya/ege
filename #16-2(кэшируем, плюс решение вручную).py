from functools import lru_cache
@lru_cache
def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * f(n - 1) + 1
for n in range (1, 3303):
    f(n)
print (f(3303)/f(3300))
#f(3303) = 3303 * f(3302) + 1 = 3303 * (3302 * f(3301) + 1) + 1 = \
#= (3303 * (3302 * (3301 * f(3300)+1)+1)+1)

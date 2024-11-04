def f(n):
    if n < 3:
        return 1
    elif n > 2 and n % 2 == 0:
        return f(n - 1) + n
    elif n > 2 and n % 2 != 0:
        return f(n - 2) + 2 * n
print (f(23)-f(21))
import sys
sys.set_int_max_str_digits(0)
def f(n):
    if n < 3:
        return 3*n
    elif n > 2 and n % 2 == 0:
        return f(n - 2) * f(n - 1) - n
    elif n > 2 and n % 2 != 0:
        return f(n - 1) - f(n - 2) + 2 * n
k = str(f(30))
print (k[-2:])

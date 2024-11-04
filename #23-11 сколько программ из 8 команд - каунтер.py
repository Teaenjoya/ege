def f(s, e, c):
    if s > e or c > 8:
        return 0
    if s == e and c == 8:
        return 1
  #  if s < e or c < 8:
    return f(s + 2, e, c + 1) + f(s + 4, e, c + 1) + f(s * 2, e, c + 1)
print (f(4,64, 0))
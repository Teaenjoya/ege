def f(st, en, ban = []):
    if st in ban or st > en:
        return 0
    if st == en:
        return 1
    if st < en:
        return f(st + 3, en, ban) + f(st + 5, en, ban) + f(st * 2, en, ban)
# print(f(4, 16) * f(16, 68, [32]))
# print(f(4, 32, [16]) * f(32, 68))
print(f(4, 16) * f(16, 68, [32])+f(4, 32, [16]) * f(32, 68))

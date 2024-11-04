def f(st, en, ban = []):
    if st in ban or st > en:
        return 0
    if st == en:
        return 1
    if st < en:
        return f(st + 1, en, ban) + f(st + 2, en, ban) + f(st * 3, en, ban)
print(f(6, 15)*f(15,25,[21])+f(6,21,[15])*f(21,25))
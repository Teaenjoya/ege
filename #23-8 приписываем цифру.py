from functools import *
@lru_cache(None)
def f(st, en):
    if st > en:
        return 0
    if st == en:
        return 1
    if st < en:
        return f(st + 2, en) + f(st * 10 + 2, en) # ну или так f(int(str(st) + '2'),en)
print (f(2,900))
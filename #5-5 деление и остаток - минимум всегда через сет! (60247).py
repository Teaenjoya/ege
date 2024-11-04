a = set()
for n in range (1,1000):
    b = bin(n)[2:]
    if n % 3 == 0:
        b += b[-3:]
    if n % 3 != 0:
        k = 3 * (n % 3)
        b += bin(k)[2:]
    r = int(b, 2)
    if r > 151:
        a.add(r)
        print(min(a))

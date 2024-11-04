m=0
for n in range (13):
    s=bin(n)[2:]
    if n % 2 == 0:
        b=s + '10'
    if n % 2 != 0:
        b = '1' + s + '00'
    r=int(b, 2)
    m = max(m, r)
    print(m)
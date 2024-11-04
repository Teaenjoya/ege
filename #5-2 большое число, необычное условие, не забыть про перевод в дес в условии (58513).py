c=set()
for n in range (1,1000001):
    b = bin(n)[2:]
    if n % 5 == 0:
        b += bin(5)[2:]
    else:
        b += '1'
    if int(b,2) % 7 == 0:
        b += bin(7)[2:]
    else:
        b += '1'
    d = int(b, 2)
    if d < 1855663:
        c.add(n)
print (max(c))

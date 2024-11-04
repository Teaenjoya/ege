for n in range (1,1001):
    b = bin(n)[2:]
    b = b + '1'
    k = b.count('1')
    if k % 2 == 0:
        b = b +'0'
    else:
        b = b +'1'
    k = b.count('1')
    if k % 2 == 0:
        b = b + '0'
    else:
        b = b + '1'
    i=int(b, 2)
    if i > 212:
        print(i)
        break
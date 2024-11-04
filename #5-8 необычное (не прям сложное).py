a=[]
for n in range (10,1001):
    s=bin(n)[3:]
    r=n-int(s,2)
    if r not in a:
        a.append(r)
print(len(a))

# for n in range (10,1001):
#     s=bin(n)[3:]
#     r=n-int(s,2)
# print(r)
# или просто сами посчитаем

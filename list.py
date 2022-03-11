n = list(range(1, 21))
b = n[:5]
m = [] 

for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)

else:
    print(m)
    print(n)

print(b)


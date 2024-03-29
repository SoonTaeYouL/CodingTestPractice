l=[i for i in range(10001)]

for i in range(9990):
    for j in str(i):
        i+=int(j)
    if i <10001:
        l[i]=0
for i in l:
    if i!=0:
        print(i)
import sys

a=list(map(int,sys.stdin.readline().rstrip()))
b=list(map(int,sys.stdin.readline().rstrip()))
l=[]
for i in range(8):
    l.append(a[i])
    l.append(b[i])

while len(l)!=2:
    ll=[]
    for i in range(len(l)-1):
        ll.append((l[i]+l[i+1])%10)
    l=ll
print(str(l[0])+str(l[1]))
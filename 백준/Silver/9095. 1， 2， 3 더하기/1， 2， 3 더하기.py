import sys
input=sys.stdin.readline
r=int(input())

for _ in range(r):
    n=int(input())
    l=[0]*(n+1)
    if n==1 or n==2: print(n)
    elif n==3: print(4)
    else:
        l[1]=1
        l[2]=2
        l[3]=4
        for i in range(4,n+1):
            l[i]=l[i-1]+l[i-2]+l[i-3]
        print(l[n])
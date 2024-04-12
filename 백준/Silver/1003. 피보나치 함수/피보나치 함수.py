import sys

input=sys.stdin.readline
num=int(input())

for _ in range(num):
    n=int(input())
    l0, l1=[1,0],[0,1]
    if n==0 or n==1:
        print(l0[n],l1[n],sep=" ")
    else:
        for i in range(2,n+1):
            l0.append(l0[i-1]+l0[i-2])
            l1.append(l1[i-1]+l1[i-2])
        print(l0[n],l1[n],sep=" ")
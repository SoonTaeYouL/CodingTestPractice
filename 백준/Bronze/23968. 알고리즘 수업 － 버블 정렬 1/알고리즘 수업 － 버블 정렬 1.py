import sys

n,k=map(int, sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))

for i in range(n-1):
    for j in range(n-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
            k-=1
            if k==0:
                print(l[j],l[j+1])
                exit()
print(-1)
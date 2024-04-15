import sys

input=sys.stdin.readline

n,k=map(int,input().split())
l=list(map(int, input().split()))
s=[0]
for i in range(1,n+1):
    s.append(s[i-1]+l[i-1])
for _ in range(k):
    i,j=map(int,input().split())
    print(s[j]-s[i-1])
import sys

input=sys.stdin.readline

a,b,n = map(int,input().split())
for i in range(n):
    a=(a%b)*10
    x=a//b
print(x)
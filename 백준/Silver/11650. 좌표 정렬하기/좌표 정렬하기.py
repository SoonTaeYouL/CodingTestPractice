import sys

input=sys.stdin.readline
n=int(input())

l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
l.sort()
for i in range(len(l)):
    print(*l[i])
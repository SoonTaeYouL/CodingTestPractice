import sys
input = sys.stdin.readline

n=int(input())
l=[]
for _ in range(n):
    a=list(input().split())
    l.append(a)
l=sorted(l,key=lambda x: (int(x[1]),int(x[0])))
for i in l:
    print(*i)
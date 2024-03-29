import sys

input=sys.stdin.readline
p,k=map(int,input().split())
l=[]
for i in range(p):
    if p%(i+1)==0:
        l.append(i+1)
if len(l)<k:
    print(0)
else:
    print(l[k-1])
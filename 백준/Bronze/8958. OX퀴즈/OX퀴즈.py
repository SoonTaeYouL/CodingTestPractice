import sys

n = int(sys.stdin.readline())

for _ in range(n):
    l,p=[],0
    str=sys.stdin.readline().rstrip()
    for i in str:
        if i =="O": l.append(i)
        else: l=[]
        p+=len(l)
    print(p)
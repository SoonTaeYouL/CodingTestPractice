import sys

n=int(sys.stdin.readline())

for _ in range(n):
    a=int(sys.stdin.readline())
    b=int(sys.stdin.readline())
    l=[t+1 for t in range(b)]
    for _ in range(a):
        for i in range(1,b):
            l[i]+=l[i-1]
    print(l[-1])
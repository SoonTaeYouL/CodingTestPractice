import sys

n = int(sys.stdin.readline())
for _ in range(n):
    a,b,c= map(int, sys.stdin.readline().split())
    h=c%a
    w=c//a+1
    if h==0:
        w-=1
        h=a
    print(h*100+w)
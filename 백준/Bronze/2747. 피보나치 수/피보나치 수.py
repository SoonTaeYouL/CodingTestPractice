import sys

n=int(sys.stdin.readline())
d = [0]*(n+1)
if n == 1 or n==2:
    d[n] = 1
    print(d[n])
else:
    d[1] = 1
    d[2] = 1
    for i in range(3,n+1):
        d[i] = d[i-1] + d[i-2]
    print(d[n])
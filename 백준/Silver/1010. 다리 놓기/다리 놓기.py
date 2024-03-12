import sys

num = int(sys.stdin.readline())
def pac(n):
    sum=1
    for i in range(2,n+1):
        sum*=i
    return sum
def ncr(n,r):
    return pac(n)//(pac(n-r)*pac(r))
for _ in range(num):
    r,n = map(int, sys.stdin.readline().split())
    print(ncr(n,r))
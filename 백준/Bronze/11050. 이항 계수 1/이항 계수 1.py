import sys

n,k = map(int, sys.stdin.readline().split())

def pac(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
print(pac(n)//(pac(n-k)*pac(k)))
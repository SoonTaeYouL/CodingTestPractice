import sys

input=sys.stdin.readline
n=int(input())
def rr(n):
    return int(n+0.5)

l=[]
if n==0: print(0)
else:
    i=rr(n*0.15)
    for _ in range(n):
        l.append(int(input()))
    l.sort()
    print(rr(sum(l[i:n-i])/(n-2*i)))
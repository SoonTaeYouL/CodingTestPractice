import sys

n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
sum=0
for i in l:
    sum+=i
print(100*sum/max(l)/n)
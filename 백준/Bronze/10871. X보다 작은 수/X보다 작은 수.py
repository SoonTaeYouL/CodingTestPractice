import sys

n,a=map(int,sys.stdin.readline().split())

l=list(map(int,sys.stdin.readline().split()))

for i in l:
    if i < a:
        print(i,end=" ")
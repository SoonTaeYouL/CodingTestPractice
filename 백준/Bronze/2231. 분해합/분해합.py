import sys

input=sys.stdin.readline

n=int(input())

i=1
while i<n:
    sum=i
    for j in str(i):
        sum+=int(j)
    if sum==n:
        print(i)
        exit()
    i+=1
print(0)
import sys

input=sys.stdin.readline
a=int(input())

max=1
for i in range(a):
    max+=6*i
    if max>=a:
        print(i+1)
        exit()
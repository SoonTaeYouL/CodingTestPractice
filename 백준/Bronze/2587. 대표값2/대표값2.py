import sys

input=sys.stdin.readline

l=[]
for _ in range(5):
    a=int(input())
    l.append(a)
l.sort()
print(int(sum(l)/5))
print(l[2])
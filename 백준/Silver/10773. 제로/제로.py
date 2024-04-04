import sys
from collections import deque

input=sys.stdin.readline
n=int(input())
q=deque()

for _ in range(n):
    a=int(input())
    if a==0: q.pop()
    else: q.append(a)
sum=0
for i in q:
    sum+=i
print(sum)
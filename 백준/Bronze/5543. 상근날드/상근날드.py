import sys

input=sys.stdin.readline

l1,l2=[],[]

for _ in range(3):
    a = int(input())
    l1.append(a)

for _ in range(2):
    a = int(input())
    l2.append(a)
print(min(l1)+min(l2)-50)
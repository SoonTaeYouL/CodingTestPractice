import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
sorted(l)
print(min(l),max(l))
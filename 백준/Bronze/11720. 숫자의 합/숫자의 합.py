import sys

n = int(sys.stdin.readline())
m = sys.stdin.readline().rstrip()
h=0
for i in m:
    h+=int(i)
print(h)
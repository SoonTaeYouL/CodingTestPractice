import sys

n = int(sys.stdin.readline())
for _ in range(n):
    s = sys.stdin.readline().rstrip().split(" ")
    for i in s:
        print(i[::-1],end=" ")
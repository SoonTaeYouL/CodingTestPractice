import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a,b = sys.stdin.readline().split()
    a=int(a)
    for i in b:
        print(i*a,end="")
    print()
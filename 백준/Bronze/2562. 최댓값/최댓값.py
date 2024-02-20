import sys

max, idx=0,0
for i in range(9):
    n = int(sys.stdin.readline())
    if n>=max:
        max=n
        idx=i+1
print(max)
print(idx)
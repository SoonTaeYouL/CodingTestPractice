import sys
input = sys.stdin.readline
max, now=0,0
for _ in range(10):
    a,b = map(int,input().split())
    now+=b-a
    if max<now:
        max=now
print(max)
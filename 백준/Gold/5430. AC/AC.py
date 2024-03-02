import sys
from collections import deque

n=int(sys.stdin.readline())
for _ in range(n):
    str=sys.stdin.readline().rstrip()
    l=int(sys.stdin.readline())
    d=deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    flag=0
    for i in str:
        if i=="R":flag+=1
        elif i=='D':
            if len(d)==0 or d[0]=="":
                print('error')
                break
            if flag%2==0:d.popleft()
            else: d.pop()
    else:
        if flag%2==0:
            print("["+",".join(d)+"]")
        else:
            d.reverse()
            print("["+",".join(d)+"]")
import sys
from collections import deque

a,n = map(int,sys.stdin.readline().split())
list = list(map(int,sys.stdin.readline().split()))
d=deque(i for i in range(1,a+1))
cnt=0
for num in list:
    while True:
        #pop
        if d[0] == num:
            d.popleft()
            break
        else:#2번
            if d.index(num)<=len(d)//2:
                d.append(d.popleft())
                cnt+=1
            #3번
            else:
                d.appendleft(d.pop())
                cnt+=1
print(cnt)
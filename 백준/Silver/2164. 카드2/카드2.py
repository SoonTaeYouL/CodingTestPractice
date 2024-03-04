import sys
from collections import deque

l=deque(i+1 for i in range(int(sys.stdin.readline())))
while len(l)>1:
    l.popleft()
    l.append(l.popleft())
print(l[0])
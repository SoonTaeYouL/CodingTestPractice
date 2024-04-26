import sys
from collections import deque
input=sys.stdin.readline
v,e,s = map(int,input().split())

visited=[0]*(v+1)
l=[]
g=[[] for _ in range(v+1)]
q=deque([s])
for _ in range(e):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

def dfs(x):
    global l
    visited[x]=1
    l.append(x)
    g[x].sort()
    for i in g[x]:
        if not visited[i]:
            dfs(i)
dfs(s)
print(*l)
visited=[0]*(v+1)
l=[s]
visited[s]=1
while q:
    n = q.popleft()
    g[n].sort()
    for i in g[n]:
        if visited[i]==0:
            q.append(i)
            visited[i]=1
            l.append(i)
print(*l)
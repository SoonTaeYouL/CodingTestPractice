import sys

input=sys.stdin.readline

a=int(input())
n=int(input())

g=[[] for _ in range(a+1)]
for _ in range(n):
    s,e=map(int,input().split())
    g[s].append(e)
    g[e].append(s)

def dfs(x):
    global cnt
    cnt+=1
    visited[x]=1
    for i in g[x]:
        if not visited[i]:
            dfs(i)
cnt=0
visited=[0]*(a+1)
dfs(1)
print(cnt-1)
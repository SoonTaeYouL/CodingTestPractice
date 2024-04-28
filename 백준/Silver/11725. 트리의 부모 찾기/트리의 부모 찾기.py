import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n=int(input())
g=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

def dfs(x):
    for i in g[x]:
        if not visited[i]:
            visited[i]=x
            dfs(i)
dfs(1)
for i in range(2,n+1):
    print(visited[i])
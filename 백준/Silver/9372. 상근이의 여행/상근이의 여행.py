import sys

input=sys.stdin.readline

num = int(input())

def dfs(x):
    global cnt
    cnt+=1
    visit[x]=1
    for i in g[x]:
        if not visit[i]:
            dfs(i)

for _ in range(num):
    n,v = map(int,input().split())
    visit=[0]*(n+1)
    g=[[] for _ in range(n+1)]
    cnt=0
    for _ in range(v):
        a,b = map(int,input().split())
        g[a].append(b)
        g[b].append(a)
    dfs(a)
    print(cnt-1)
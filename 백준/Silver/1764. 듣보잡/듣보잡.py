import sys

input=sys.stdin.readline
n,m=map(int,input().split())
dic={}
l=[]
for _ in range(n+m):
    s=input().rstrip()
    if s in dic:
        dic[s]+=1
    else:
        dic[s]=1
for k,v in dic.items():
    if v==2:
        l.append(k)
l.sort()
print(len(l))
print(*l,sep="\n")
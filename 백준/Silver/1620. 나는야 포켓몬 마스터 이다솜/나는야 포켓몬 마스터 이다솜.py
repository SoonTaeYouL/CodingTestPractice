import sys

n,q=map(int,sys.stdin.readline().split())
dic = {}
for i in range(n):
    a=sys.stdin.readline().rstrip()
    dic[i+1]=a
    dic[a]=i+1

for _ in range(q):
    a=sys.stdin.readline().rstrip()
    if a.isdigit():
        print(dic[int(a)])
    else:
        print(dic[a])
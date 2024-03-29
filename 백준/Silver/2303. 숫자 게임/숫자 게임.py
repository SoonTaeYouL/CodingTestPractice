import sys

input=sys.stdin.readline
n=int(input())
max_l=[]
for _ in range(n):
    l=list(map(int,input().split()))
    m=0
    for i in range(5):
        for j in range(i+1,5):
            for k in range(j+1,5):
                if (l[i]+l[j]+l[k])%10 > m:
                    m=(l[i]+l[j]+l[k])%10
    max_l.append(m)

for i in range(n-1,-1,-1):
    if max_l[i] == max(max_l):
        print(i+1)
        break
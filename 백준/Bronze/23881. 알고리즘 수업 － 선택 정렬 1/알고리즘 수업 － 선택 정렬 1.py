import sys

n,k=map(int ,sys.stdin.readline().split())
l=list(map(int, sys.stdin.readline().split()))
'''
31245
'''
cnt=0
for i in range(n-1,-1,-1):
    max_i=l.index(max(l[0:i+1]))
    if max_i != i:
        l[max_i], l[i] = l[i], l[max_i]
        cnt+=1
    if cnt==k:
            print(l[max_i],l[i])
            break
else: print(-1)
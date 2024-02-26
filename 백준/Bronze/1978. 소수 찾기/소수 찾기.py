import sys

n=int(sys.stdin.readline())
cnt=0

def sosu(n):
    global cnt
    if n==1:
        return
    for i in range(2,n):
        if n%i==0: break
    else:
        cnt+=1

l=list(map(int,sys.stdin.readline().split()))
for i in l:
    sosu(i)
print(cnt)
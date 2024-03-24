import sys

# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10
dic={}
new=[]
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
n2=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
for i in a:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for i in l:
    if i in dic:
        new.append(dic[i])
    else:
        new.append(0)
print(*new)

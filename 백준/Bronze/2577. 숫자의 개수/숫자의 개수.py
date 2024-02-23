import sys
d={}
list = [0 for _ in range(10)]
sum=1
for i in range(3):
    a=int(sys.stdin.readline())
    sum*=a
s=str(sum)
for i in s:
    if i in d:
        d[i]+=1
    else: d[i]=1

for k,v in d.items():
    list[int(k)]=v
for j in list:
    print(j)
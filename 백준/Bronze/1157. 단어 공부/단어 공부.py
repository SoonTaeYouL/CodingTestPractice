import sys

s = sys.stdin.readline().rstrip().upper()
l=list(set(s))
cnt=[]
for i in l:
    cnt.append(s.count(i))
if cnt.count(max(cnt))>=2: print("?")
else:
    print(l[cnt.index(max(cnt))])
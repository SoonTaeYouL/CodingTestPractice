import sys

n = int(sys.stdin.readline())
dic={}
for _ in range(n):
    a=sys.stdin.readline().rstrip()
    if len(a) not in dic:
        dic[len(a)]=[a]
    elif a in dic[len(a)]:
        continue
    else:
        dic[len(a)].append(a)
dic = dict(sorted(dic.items()))
for v in dic.values():
    v.sort()
    for i in v:
        print(i)
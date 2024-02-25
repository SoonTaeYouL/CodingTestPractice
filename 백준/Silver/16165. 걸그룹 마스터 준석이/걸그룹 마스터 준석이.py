import sys

dic={}
n, q = map(int,sys.stdin.readline().split())

for _ in range(n):
    a=sys.stdin.readline().rstrip()
    num=int(sys.stdin.readline())
    l = list(sys.stdin.readline().rstrip() for _ in range(num))
    l.sort()
    dic[a]=l

for _ in range(q):
    str=sys.stdin.readline().rstrip()
    flag=int(sys.stdin.readline())
    if flag==1:
        for k,v in dic.items():
            if str in v:
                print(k)
    else:
        for i in dic[str]:
            print(i)
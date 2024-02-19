import sys

n = int(sys.stdin.readline())

for t in range(n):
    v= sys.stdin.readline().rstrip()
    list = []
    for i in v:
        if i == "(": list.append(i)
        elif i == ")":
            if len(list)!=0:
                list.pop()
            else:
                print("NO")
                break
    else:
        if len(list)==0: print("YES")
        else: print('NO')
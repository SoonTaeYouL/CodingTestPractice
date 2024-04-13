import sys

input=sys.stdin.readline
'''
1, 1, 1, 2, 2, 3, 4, 5, 7, 9
'''
n=int(input())

for _ in range(n):
    i = int(input())
    l=[0,1,1]
    if i==1 or i==2:
        print(l[i])
    else:
        for j in range(3,i+1):
            l.append(l[j-2]+l[j-3])
        print(l[i])
import sys

while True:
    l=list(map(int,sys.stdin.readline().split()))
    l.sort()
    if l[0]==0 and l[1]==0 and l[2]==0:
        break
    else:
        if l[0]**2+l[1]**2==l[2]**2:
            print('right')
        else:
            print('wrong')
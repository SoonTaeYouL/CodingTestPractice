import sys

while True:
    s=sys.stdin.readline().rstrip()
    l=[]
    if s=='.':
        break
    for i in s:
        if i=='[' or i=='(':
            l.append(i)
        elif i==']':
            if len(l)!=0 and l[-1]=='[':
                l.pop()
            else:
                l.append(i)
                break
        elif i==')':
            if len(l)!=0 and l[-1]=='(':
                l.pop()
            else:
                l.append(i)
                break
    if len(l)==0:
        print('yes')
    else:
        print('no')
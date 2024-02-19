import sys

n = int(sys.stdin.readline())
q=[]
for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == 'push': q.append(int(s[1]))
    elif s[0] == 'pop':
        if len(q)==0: print(-1)
        else:
            print(q.pop(0))
            #q.pop(0)
    elif s[0] == 'size': print(len(q))
    elif s[0] == 'empty':
        if len(q)==0: print(1)
        else: print(0)
    elif s[0] == 'front':
        if len(q)==0: print(-1)
        else: print(q[0])
    elif s[0] == 'back':
        if len(q)==0: print(-1)
        else: print(q[-1])

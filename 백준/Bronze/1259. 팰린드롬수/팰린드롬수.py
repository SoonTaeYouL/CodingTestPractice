import sys

while True:
    s=sys.stdin.readline().rstrip()
    if s=='0': break
    else:
        for i in range(len(s)//2):
            if s[i]!=s[-1*(i+1)]:
                print('no')
                break
        else:print('yes')
import sys

while True:
    s = sys.stdin.readline().split()
    if s[0]=="#": break
    if int(s[1])>17 or int(s[2])>=80:
        print(f'{s[0]} Senior')
    else: print(f'{s[0]} Junior')
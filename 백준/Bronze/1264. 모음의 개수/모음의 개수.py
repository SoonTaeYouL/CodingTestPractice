import sys

list = ['a','e','i','o','u','A','E','I','O','U']

while True:
    cnt=0
    str = sys.stdin.readline().rstrip()
    if str == '#':break
    for i in str:
        if i in list: cnt +=1
    print(cnt)
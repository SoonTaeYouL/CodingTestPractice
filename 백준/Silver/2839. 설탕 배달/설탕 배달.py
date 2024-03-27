import sys

input=sys.stdin.readline
n=int(input())

'''
ex) 18일때 5로 나누면 3.x => 5가 3번일떄 2번일떄 1번일때 없을떄로 나눔=> 재귀
'''

c=n//5
for i in range(c,-1,-1):
    if (n-5*i)%3==0:
        print(i+(n-5*i)//3)
        break
else:
    print(-1)
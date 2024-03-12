import sys

'''
n=1 일 때 1가지
n=2 일 때 11, 2 -> 2가지
n=3 일 때 111,12,21 => 3가지
n=4 일 때 1111,112,121,211,22 => 5가지
n=5 일 때 11111,1112,1121,1211,2111,122,212,221 => 8가지
'''

n=int(sys.stdin.readline())
list=[0]*(n+1)
if n==1 or n==2:
    print(n)
else:
    list[1]=1
    list[2]=2
    for i in range(3,n+1):
        list[i]=list[i-1]+list[i-2]
    print(list[n]%10007)
import sys

input=sys.stdin.readline

n=int(input())

'''
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
0 0 1 1 2 3 2 3 3 2 3  4  3  4  4  4
'''

l=[0]*(n+1)

for i in range(2,n+1):
    l[i]=l[i-1]+1
    if i%3==0:
        l[i]=min(l[i//3]+1,l[i])
    if i%2==0:
        l[i]=min(l[i//2]+1,l[i])
print(l[n])
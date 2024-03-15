import sys
'''
n=3
7
1 3
1 2
3 2
1 3
2 1
2 3
1 3
'''
n=int(sys.stdin.readline())
print(2**n-1)
def hanoi(n,a,c,b):
    if n==1: print(a,c)
    else:
        hanoi(n-1,a,b,c)
        print(a,c)
        hanoi(n-1,b,c,a)
if n<=20:hanoi(n,1,3,2)
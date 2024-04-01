import sys
input=sys.stdin.readline

n=int(input())
s=input().rstrip()
sum=0
for i in range(n):
    sum+= (ord(s[i])-96)*(31**i)
print(sum%1234567891)
import sys, math

input=sys.stdin.readline

a,b,v=map(int,input().split())
n=a-b
v=v-a

print(math.ceil(v/n)+1)
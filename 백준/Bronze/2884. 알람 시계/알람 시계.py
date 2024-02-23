import sys

a,b = map(int,sys.stdin.readline().split())
if b>=45: print(a,b-45)
elif a==0 and b<45: print(23,60+b-45)
elif b<45: print(a-1,60+b-45)
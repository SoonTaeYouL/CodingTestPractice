import sys

a=list(map(int,sys.stdin.readline().split()))
if a==sorted(a): print("ascending")
elif sorted(a,reverse=True)==a: print('descending')
else: print('mixed')
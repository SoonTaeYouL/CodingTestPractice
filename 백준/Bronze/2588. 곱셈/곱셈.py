import sys

input = sys.stdin.readline
a = int(input())
b = input()

x=a * int(b[2])
y=a * int(b[1])
z=a * int(b[0])
print(x)
print(y)
print(z)
print(x+10*y+100*z)
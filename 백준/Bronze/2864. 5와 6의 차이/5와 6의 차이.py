import sys
input = sys.stdin.readline

a,b = map(str, input().split())
a = a.replace('6','5')
b = b.replace('6','5')
print(int(a)+int(b))
a = a.replace('5','6')
b = b.replace('5','6')
print(int(a)+int(b))
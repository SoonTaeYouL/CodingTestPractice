import sys

list=[]
for i in range(10):
    a=int(sys.stdin.readline())
    list.append(a%42)
print(len(set(list)))
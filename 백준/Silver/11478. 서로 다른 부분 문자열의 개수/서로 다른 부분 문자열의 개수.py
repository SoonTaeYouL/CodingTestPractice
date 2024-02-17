import sys

str = sys.stdin.readline()
list = set()

for i in range(len(str)):
    for j in range(len(str)-i):
        list.add(str[i:j+i])
print(len(list)-1)
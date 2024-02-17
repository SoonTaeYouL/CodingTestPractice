import sys

list=[0]*26
str = input()
for i in str:
    list[ord(i)-97]+=1
print(*list)
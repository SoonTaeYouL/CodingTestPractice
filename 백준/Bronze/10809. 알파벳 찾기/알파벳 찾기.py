list=[-1]*26
str = input()
c=0
notin = []
for i in str:
    if i not in notin:
        notin.append(i)
        list[ord(i)-97]=c
    c+=1
print(*list)
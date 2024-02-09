n = int(input())
sen = [input().split() for _ in range(n)]
new = []
for i in sen:
    list = []
    for j in range(len(i)):
        list.append(i[len(i)-j-1])
    new.append(list)
for x in range(n):
    print(f"Case #{x+1}:",*new[x])
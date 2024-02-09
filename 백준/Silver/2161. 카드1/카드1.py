list =[i+1 for i in range(int(input()))]
ans , i= [] , 0
while len(list)>0:
    ans.append(list[i])
    list.remove(list[i])
    if len(list)==0: break
    list.append(list[i])
    list.remove(list[i])
print(*ans)
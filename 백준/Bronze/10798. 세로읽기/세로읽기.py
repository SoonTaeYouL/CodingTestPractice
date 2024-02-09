list = [input() for _ in range(5)]
a = ""
for i in range(15):
    for j in range(5):
        if len(list[j])>i:
            print(list[j][i],end='')

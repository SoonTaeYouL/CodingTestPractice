def solution(name, yearning, photo):
    answer = []
    dic = {name[i] : yearning[i] for i in range(len(name))}
    print(dic)
    for i in photo:
        hap=0
        for j in range(len(i)):
            if i[j] in name:
                hap += dic[i[j]]
        answer.append(hap)
    return answer
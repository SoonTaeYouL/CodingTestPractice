def solution(participant, completion):
    answer = ''
    dic = {}
    for i in participant:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] +=1
    for i in completion:
        if i in dic:
            dic[i] -=1
    for k, v in dic.items():
        if v ==1:
            answer+=k
    return answer
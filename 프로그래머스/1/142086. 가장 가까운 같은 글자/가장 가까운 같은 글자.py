def solution(s):
    answer = []
    list =[]
    for i in range(len(s)):
        if s[i] not in list:
            answer.append(-1)
            list.append(s[i])
        else:
            l = list[::-1]
            for j in range(len(l)):
                if l[j] ==s[i]:
                    answer.append(j+1)
                    list.append(s[i])
                    break
                    
    return answer
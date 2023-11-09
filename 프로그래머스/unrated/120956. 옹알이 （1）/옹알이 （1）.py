def solution(babbling):
    answer = 0
    list = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for j in list:
            if j in babbling[i]:
                babbling[i] = babbling[i].replace(j," ")
    for i in babbling:
        if i == " " or i =="  " or i =="   " or i =="    ":
            answer+=1
        
    return answer
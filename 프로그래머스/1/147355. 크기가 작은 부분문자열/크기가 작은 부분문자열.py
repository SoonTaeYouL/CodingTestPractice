def solution(t, p):
    answer = 0
    list=[]
    for i in range(len(t)-len(p)+1):
        list.append(t[i:i+len(p)])
    for i in list:
        if int(i)<=int(p):
            answer+=1
        
    return answer
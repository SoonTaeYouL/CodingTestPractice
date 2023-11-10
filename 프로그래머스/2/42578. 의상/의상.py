def solution(clothes):
    answer = 1
    dic = {i[1]: [] for i in clothes}
    list=[] 
    m = 1
    for v in clothes: 
        dic[v[1]].append(v[0])
    for k,v in dic.items():
        answer *= (len(v)+1)
    return answer-1
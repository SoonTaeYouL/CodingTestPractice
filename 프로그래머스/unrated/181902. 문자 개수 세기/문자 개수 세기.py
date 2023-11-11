def solution(my_string):
    answer = []
    dic = {chr(i):0 for i in range(65,91)}
    dic2 = {chr(j):0 for j in range(97,123)}
    dic.update(dic2)
    for i in my_string:
        dic[i] +=1
    return [v for v in dic.values()]
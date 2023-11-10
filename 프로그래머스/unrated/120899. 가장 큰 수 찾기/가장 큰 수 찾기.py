def solution(array):
    answer = []
    max=0
    ii=0
    for i in range(len(array)):
        if max > array[i]: max = max
        else: 
            max = array[i]
            ii = i
    answer.append(max)
    answer.append(ii)
    return answer
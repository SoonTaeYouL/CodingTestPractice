def solution(X, Y):
    answer = ''
    x = {str(i):0 for i in range(9,-1,-1)}
    y = {str(i):0 for i in range(9,-1,-1)}
    for i in X:
        x[i] +=1
    for i in Y:
        y[i] +=1
    for i in range(9,-1,-1):
        answer += str(i) * min(x[str(i)],y[str(i)])
    if answer =='': return '-1'
    elif len(answer) == answer.count('0'): return "0"
    return answer
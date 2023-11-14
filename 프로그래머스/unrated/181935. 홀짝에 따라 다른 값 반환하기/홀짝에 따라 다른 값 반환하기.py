def solution(n):
    answer = 0
    for i in range((n+1)//2):
        if n%2==0:
            answer += (2*i+2)**2
        else:
            answer += 2*i+1
    return answer
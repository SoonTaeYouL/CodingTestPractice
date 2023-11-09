def solution(num, total):
    answer = []
    n = total//num 
    if num%2 ==0:
        for i in range(n-(num//2)+1,n+(num//2)+1):
            answer.append(i)
    else:
        for i in range(n-(num//2),n+(num//2)+1):
            answer.append(i)
    return answer
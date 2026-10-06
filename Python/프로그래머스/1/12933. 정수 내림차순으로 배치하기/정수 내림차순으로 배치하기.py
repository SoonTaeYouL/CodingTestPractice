def solution(n):
    s = ""
    answer = list(str(n))
    answer.sort(reverse=True)
    for i in answer:
        s +=str(i)
    return int(s)
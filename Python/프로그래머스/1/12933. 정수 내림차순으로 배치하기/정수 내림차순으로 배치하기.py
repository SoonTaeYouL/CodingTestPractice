def solution(n):
    s = ""
    answer = [int(i) for i in str(n)]
    answer.sort(reverse=True)
    for i in answer:
        s +=str(i)
    return int(s)
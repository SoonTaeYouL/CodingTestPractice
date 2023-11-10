def solution(s):
    answer = 0
    s = s.split(" ")
    pre = 0
    for i in s:
        if i == "Z":
            answer -= pre
        else:
            answer += int(i)
            pre = int(i)
    return answer
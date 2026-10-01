def solution(s):
    answer = True
    n=0
    for i in s:
        if i == "(":
            n += 1
        else :
            n -= 1
        if s[0] == ")" or n<0:
            return False
    if n != 0 : answer = False
    return answer
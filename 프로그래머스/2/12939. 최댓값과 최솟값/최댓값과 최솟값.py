def solution(s):
    answer = ''
    s = list(map(int, s.split(" ")))
    s.sort()
    l=len(s)
    return f'{s[0]} {s[l-1]}'
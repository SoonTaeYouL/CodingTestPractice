def solution(a, d, included):
    answer = 0
    s=a
    for i in included:
        if i ==True:
            answer+=s
        s+=d
    return answer
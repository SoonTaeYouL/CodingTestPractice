def solution(sizes):
    answer = 0
    maxL,minL = [], []
    for i in sizes:
        maxL.append(max(i))
        minL.append(min(i))
    return max(maxL) * max(minL)
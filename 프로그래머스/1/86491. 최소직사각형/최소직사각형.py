def solution(sizes):
    answer = 0
    max=[0,0]
    for i in sizes:
        i.sort()
        if max[0]<i[0]:
            max[0]=i[0]
        if max[1]<i[1]:
            max[1]=i[1]
    return max[0]*max[1]
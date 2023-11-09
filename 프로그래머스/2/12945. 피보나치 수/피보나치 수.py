def solution(n):
    answer = 0
    f = [0,1,1]
    for i in range(n+1):
        if i >=3:
            f.append(f[i-2]+f[i-1])
    answer = f[n]%1234567
    return answer
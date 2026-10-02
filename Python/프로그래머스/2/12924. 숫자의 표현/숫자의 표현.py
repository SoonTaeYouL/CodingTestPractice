def solution(n):
    answer = 0
    
    si = 1
    while si<=n:
        sum = 0
        for i in range(si,n+1):
            sum += i
            if sum >= n:
                if sum == n:
                    answer +=1
                break
        si +=1
        
    return answer
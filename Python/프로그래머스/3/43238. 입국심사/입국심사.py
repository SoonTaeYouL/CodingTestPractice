def solution(n, times):
    answer = 0
    
    s , e = 1, min(times)*n # 1~42
    
    while s<=e:
        mid = (s+e)//2
        
        cnt = 0
        
        for t in times:
            cnt += mid//t # 21//7 21//10 
        
        if cnt < n:
            s = mid + 1
        else :
            e = mid - 1
    return s
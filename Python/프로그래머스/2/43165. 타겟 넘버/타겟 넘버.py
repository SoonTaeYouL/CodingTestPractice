def solution(numbers, target):
    answer = 0
    
    def dfs(v, sum):
        nonlocal answer
        
        if v == len(numbers):
            if sum == target:
                answer +=1
            return
        
        dfs(v+1,sum+numbers[v])
        dfs(v+1,sum-numbers[v])
    
    dfs(0,0)
    return answer
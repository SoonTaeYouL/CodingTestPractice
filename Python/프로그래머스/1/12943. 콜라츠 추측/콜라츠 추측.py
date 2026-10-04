def solution(num):
    cnt = 0 # 시행횟수
    if num == 1:
        return 0
    
    while cnt<= 500:
        if num == 1:
            return cnt
        else:
            if num%2==0:
                num = num/2
                cnt +=1
            else :
                num = num*3 + 1
                cnt +=1 
    return -1
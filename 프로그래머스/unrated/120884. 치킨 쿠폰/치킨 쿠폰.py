def solution(chicken):
    answer = 0
    while chicken>=10:
        if chicken >=10:
            a = chicken//10
            chicken += a
            answer += a
            chicken -= 10*a

            
    return answer
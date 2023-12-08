def solution(balls, share):
    answer = pac(balls)/(pac(balls-share)*pac(share))
    return answer
def pac(n):
    hap=1
    for i in range(1,n+1):
        hap*=i
    return hap
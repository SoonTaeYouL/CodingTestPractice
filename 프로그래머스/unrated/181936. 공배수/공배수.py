def solution(number, n, m):
    answer = 0
    if number%n==0:
        print(answer)
        if number%m==0:
            print(answer)
            answer = 1
    return answer
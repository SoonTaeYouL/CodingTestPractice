def solution(my_str, n):
    answer = []
    if len(my_str)%n !=0:
        for i in range(len(my_str)//n):
            answer.append(my_str[n*i:n*i+n])
        answer.append(my_str[(len(my_str)//n)*n:])
    else:
        for i in range(len(my_str)//n):
            print(my_str[n*i:n*i+n])
            answer.append(my_str[n*i:n*i+n])
    return answer
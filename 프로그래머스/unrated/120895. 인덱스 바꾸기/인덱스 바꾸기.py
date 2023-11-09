def solution(my_string, num1, num2):
    s = my_string
    list = []
    answer = ''
    for i in range(len(s)):
        list.append(s[i])
    for i in range(len(list)):
        if i == num1:
            answer += list[num2]
        elif i == num2:
            answer += list[num1]
        else:
            answer += list[i]
    return answer
def solution(my_string):
    answer = 0
    a = my_string.split(" ")
    answer += int(a[0])
    for i in range(len(a)):
        if a[i] == "+":
            answer += int(a[i+1])
        elif a[i] == "-":
            answer -= int(a[i+1])
    return answer
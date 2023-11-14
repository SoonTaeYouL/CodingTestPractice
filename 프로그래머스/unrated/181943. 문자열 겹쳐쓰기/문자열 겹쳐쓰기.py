def solution(my_string, overwrite_string, s):
    answer = ''
    n = len(my_string)-len(overwrite_string)-s
    m = len(my_string)
    answer += my_string[0:s] + overwrite_string + my_string[m-n:m]
    return answer

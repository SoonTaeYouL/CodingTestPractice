def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i]=="l":
            return str_list[0:i]
            break
        if str_list[i]=="r":
            return str_list[i+1:]
            break
    if "l" or "r" not in str_list:
        return []
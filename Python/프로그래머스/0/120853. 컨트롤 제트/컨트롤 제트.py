def solution(s):
    l = s.split(" ")
    new = []
    for i in l:
        if i == "Z":
            new.pop()
        else:
            new.append(int(i))
    return sum(new)
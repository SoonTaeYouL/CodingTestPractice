def solution(s):
    answer = -1
    stack = []
    
    for i in s:
        if stack==[]:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    return 1 if stack==[] else 0
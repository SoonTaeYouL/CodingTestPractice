# def solution(A, B):
#     answer = -1
#     a = []
#     for i in range(len(A)):
#         a.append(max(A))
#         A.remove(max(A))
#     print(a)
#     return answer
def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    for a in A:
        if a >= B[0]:
            continue
        else:
            answer += 1
            del B[0]
    return answer


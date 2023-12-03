def solution(q, r, code):
    return code[r::q]

# index를 q로 나눈 나머지가 r이면 index=q*무언가 + r
# r부터 시작해서 q만큼 반복
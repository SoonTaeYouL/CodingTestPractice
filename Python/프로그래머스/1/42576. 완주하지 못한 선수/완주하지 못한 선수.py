# 참가 p, 완주 c -> 완주 못한 선수 이름을 반환
# 참가자 중에 완료자가 있으면 삭제
from collections import Counter

def solution(participant, completion):
    
    answer = Counter(participant)-Counter(completion)
    return list(answer.keys())[0]
def solution(s):
    answer = [0,0]
    for i in range(5):
        zn = 0
        # 0 개수 세기
        for i in s:
            if int(i)==0:
                zn +=1
        answer[1] += zn
        
        if (len(s)-zn)==1:
            answer[0] +=1
            return answer
        # 남은 길이를 이진 변환
        s = bin(len(s)-zn)[2:]
        answer[0] +=1

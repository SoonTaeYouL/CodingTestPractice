def solution(answers):
    answer = []
    s1 = [1,2,3,4,5]*(len(answers)//5+1)
    s2 = [2,1,2,3,2,4,2,5]*(len(answers)//8+1)
    s3 = [3,3,1,1,2,2,4,4,5,5]*(len(answers)//10+1)
    score = {1:0,2:0,3:0}
    for i in range(len(answers)):
        if answers[i] == s1[i]:
            score[1] +=1
        if answers[i] == s2[i]:
            score[2] +=1
        if answers[i] == s3[i]:
            score[3] +=1
    for k,v in score.items():
        if max(score.values()) == v:
            answer.append(k)
    
    return answer
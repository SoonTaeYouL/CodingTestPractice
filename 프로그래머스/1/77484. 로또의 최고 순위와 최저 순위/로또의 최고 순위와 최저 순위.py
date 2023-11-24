def solution(lottos, win_nums):
    answer = []
    win = 7
    zero = 0
    for i in lottos:
        if i in win_nums:
            win -=1
        if i ==0:
            zero +=1
    if (win==7 or win==6) and zero==0: return [6,6]
    if win==7 and zero==1: return [6,6]
    if win==7 and zero==6: return [1,6]
    answer.append(win-zero)
    answer.append(win)
    print(win)
    return answer
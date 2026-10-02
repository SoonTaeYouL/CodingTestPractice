def solution(hp):
    answer = 0
    n1 = hp//5
    n2 = (hp-n1*5)//3
    n3 = (hp-n1*5-n2*3)
    return n1+n2+n3
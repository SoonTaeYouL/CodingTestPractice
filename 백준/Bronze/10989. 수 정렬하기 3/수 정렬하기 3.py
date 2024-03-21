import sys

n=int(sys.stdin.readline())
l=[0]*(10001) # 배열 생성

#input이자 인덱스에 개수 추가
for _ in range(n):
    l[int(sys.stdin.readline())]+=1
#현재 l의 숫자가 인덱스의 개수

#배열에서 0이 아닌 인덱스값 프린트
for i in range(len(l)):
    if l[i]!=0:
        for _ in range(l[i]):
            print(i)
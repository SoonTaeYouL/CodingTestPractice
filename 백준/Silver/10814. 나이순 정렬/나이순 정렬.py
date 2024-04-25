import sys

input=sys.stdin.readline

n = int(input())
l=[]
for _ in range(n):
    l.append(list(input().split()))
l.sort(key=lambda x: int(x[0]))
# sort에 key를 사용하여 정렬할 기준을 정해줄 수 있다.
# lambda x: int(x[0])은 x의 0번째 인덱스를 int로 변환하여 정렬한다.
# x[0]은 나이이므로 나이순으로 정렬한다.
for i in l:
    print(i[0],i[1])
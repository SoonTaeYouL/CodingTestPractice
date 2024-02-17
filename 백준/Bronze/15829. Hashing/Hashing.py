import sys

n = int(sys.stdin.readline())
sum , cnt = 0, 0
for i in sys.stdin.readline().rstrip():
    sum+=(ord(i)-96) * ((31)**(cnt))
    cnt+=1
print(sum)
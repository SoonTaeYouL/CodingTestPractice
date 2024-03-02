import sys

# def ho(a,b):
#     hap=0
#     if a==0:
#         return b
#     else:
#         for i in range(1,b+1):
#             hap+=ho(a-1,i)
#         return hap

n=int(sys.stdin.readline())
for _ in range(n):
    a=int(sys.stdin.readline())
    b=int(sys.stdin.readline())
    l=[i for i in range(1,b+1)]
    for i in range(a):
        for j in range(1,b):
            l[j]+=l[j-1]
    print(l[-1])
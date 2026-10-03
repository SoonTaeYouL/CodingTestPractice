from collections import Counter

def solution(nums):
    answer = 0
    n = len(nums)//2
    h = Counter(nums)
    return len(h) if len(h)<=n else n
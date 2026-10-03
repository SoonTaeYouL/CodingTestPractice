from collections import Counter

def solution(nums):
    
    return len(Counter(nums)) if len(Counter(nums))<=(len(nums)//2) else (len(nums)//2)
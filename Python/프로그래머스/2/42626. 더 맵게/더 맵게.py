import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        if scoville[0] >=K:
            return answer
        
        if len(scoville) < 2:
            return -1
        
        n1 = heapq.heappop(scoville)
        n2 = heapq.heappop(scoville)
        n = n1 + n2*2
        heapq.heappush(scoville,n)
        answer += 1
        

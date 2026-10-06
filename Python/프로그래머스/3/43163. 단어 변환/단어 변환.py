from collections import deque

def solution(begin, target, words):
    # [조건 체크] 목표 단어(target)가 단어 목록(words)에 없다면 변환 자체가 불가능합니다.
    if target not in words:
        return 0
    
    # 변환이 가능한 경우에만 본격적으로 BFS 함수를 실행합니다.
    return bfs(begin, target, words)
    
def bfs(begin, target, words):
    # 1. 큐(Queue) 선언 및 초기화
    q = deque()
    # 큐에 [현재 단어, 현재까지의 변환 횟수]를 리스트 형태로 담아줍니다.
    # 시작 단계이므로 변환 횟수는 0입니다.
    q.append([begin, 0])
    
    # 2. 방문 기록(visited) 세트 생성
    # 한 번 탐색한 단어를 다시 탐색하면 무한 루프에 빠지므로, 방문한 단어를 저장해 둡니다.
    # 시작 단어인 begin은 이미 방문한 것이므로 먼저 넣어줍니다.
    visited = set([begin])
    
    # 3. 큐가 빌 때까지 반복 (더 이상 변환할 단어가 없을 때까지)
    while q:
        # 큐의 맨 앞(가장 먼저 들어온 것)에서 단어와 현재까지의 변환 횟수를 꺼냅니다.
        now, step = q.popleft()
        
        # [정답 확인] 현재 꺼낸 단어가 우리가 찾던 target 단어와 같다면
        # BFS 특성상 가장 먼저 도달한 이 순간이 '최소 변환 횟수'이므로 즉시 반환합니다.
        if now == target:
            return step
        
        # 4. 단어 목록(words)을 하나씩 순회하며 다음으로 변환할 수 있는 단어 찾기
        for w in words:
            # 아직 방문하지 않은 단어일 때만 변환 가능성을 검사합니다.
            if w not in visited:
                cnt = 0  # 두 단어 간에 '서로 다른 글자의 개수'를 저장할 변수
                
                # 단어의 길이만큼 인덱스(0, 1, 2...)를 돌며 한 글자씩 비교합니다.
                for i in range(len(w)):
                    # 현재 단어(now)의 i번째 글자와 후보 단어(w)의 i번째 글자가 다르면
                    if now[i] != w[i]:
                        cnt += 1  # 다른 글자 수 1 증가
                
                # [변환 조건] 서로 다른 글자가 '정확히 1개'일 때만 변환할 수 있습니다.
                if cnt == 1:
                    # 다음 탐색을 위해 큐에 [새 단어, 변환 횟수 + 1]을 넣어줍니다.
                    q.append([w, step + 1])
                    # 이 단어는 탐색 목록에 올렸으므로 방문 처리를 하여 중복 방지를 합니다.
                    visited.add(w)
                    
    # 큐가 빌 때까지 돌았는데도 target을 만나지 못했다면 변환할 수 없는 구조이므로 0을 반환합니다.
    return 0
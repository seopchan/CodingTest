from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])
    
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # UDLR
    visited = [[-1] * m for _ in range(n)]
    
    q = deque()
    
    sr, sc = 0, 0 # 로봇 시작점
    gr, gc = 0, 0 # 목적지
    for r_idx, r in enumerate(board):
        if 'R' in r:
            sr, sc = r_idx, r.index('R')
        if 'G' in r:
            gr, gc = r_idx, r.index('G')
    
    q.append((sr, sc))
    visited[sr][sc] = 0
    
    while q:
        r, c = q.popleft()
        
        # 도착지점인지 확인
        if r == gr and c == gc:
            break;
        
        for dr, dc in dir:
            nr, nc = r, c
            # 벽이나 장애물이 나올 때까지 이동
            while 0 <= nr + dr < n and 0 <= nc + dc < m and board[nr + dr][nc + dc] != 'D':
                nr += dr
                nc += dc
            
            # 유효 위치 확인, 방문 확인
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == -1:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    
    return visited[gr][gc]
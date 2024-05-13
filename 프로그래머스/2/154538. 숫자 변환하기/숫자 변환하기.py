from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    que = deque([(x, 0)])
    visited = set()
    visited.add(x)
    
    while que:
        cur_num, h = que.popleft()
        
        for next_num in (cur_num + n, cur_num * 2, cur_num * 3):
            if next_num == y:
                return h + 1
            
            if next_num < y and next_num not in visited:
                visited.add(next_num)
                que.append((next_num, h + 1))
            
    return -1
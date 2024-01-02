from collections import deque

def solution(priorities, location):
    m = max(priorities)
    queue = deque(priorities)
    
    count = 0
    while len(queue) > 0:
        p = queue.popleft()

        if p >= m:
            count += 1
            
            if location == 0:
                return count
            else:
                location -= 1
            m = max(queue)    
        else:
            queue.append(p)
            
            if location == 0:
                location = len(queue) - 1
            else:
                location -= 1
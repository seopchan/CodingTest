from collections import deque

def solution(queue1, queue2):
    q1 = sum(queue1)
    q2 = sum(queue2)
    l = len(queue1)
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    sumVal = q1 + q2
    
    if sumVal % 2 == 1:
        return -1
    
    count = 0
    while q1 != q2:
        if q1 == 0 or q2 == 0 or count > l * 2.5:
            count = -1
            break
        
        if q1 > q2:
            val = queue1.popleft()
            q1 -= val
            
            queue2.append(val)
            q2 += val
            
        else:
            val = queue2.popleft()
            q2 -= val
                
            queue1.append(val)
            q1 += val
                
        count += 1
    
    return count
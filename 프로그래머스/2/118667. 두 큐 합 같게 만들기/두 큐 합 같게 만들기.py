def solution(queue1, queue2):
    q1 = 0
    q2 = 0
    sum = 0
    l = len(queue1)
    for i in range(0, l):
        q1 += queue1[i]
        q2 += queue2[i]
        sum += queue1[i] + queue2[i]
    
    if (q1+q2)%2 == 1:
        return -1
    
    count = 0
    while q1 != q2:
        if q1 == 0 or q2 == 0 or count > l * 2.5:
            count = -1
            break
        
        if q1 > q2:
            val = queue1.pop(0)
            q1 -= val
            
            queue2.append(val)
            q2 += val
            
            count += 1
        else:
            val = queue2.pop(0)
            q2 -= val
                
            queue1.append(val)
            q1 += val
                
            count += 1
    
    return count
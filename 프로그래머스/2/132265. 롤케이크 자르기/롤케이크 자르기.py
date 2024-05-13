def solution(topping):
    answer = 0
    left = set()
    right = set(topping)
    
    # 첫 토핑 상태 초기화 0:n
    right_count = {}
    for t in topping:
        if t in right_count:
            right_count[t] += 1
        else:
            right_count[t] = 1
    
    # 토핑을 순회하며 개수 비교
    for t in topping:
        left.add(t)
        
        right_count[t] -= 1
        if right_count[t] == 0:
            right.remove(t)
        
        if len(left) == len(right):
            answer += 1
        
    return answer
    
    
    return answer
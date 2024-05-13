from collections import defaultdict

def solution(topping):
    answer = 0
    left = defaultdict(int)
    right = defaultdict(int)
    
    # 첫 토핑 상태 초기화 0:n
    for t in topping:
        right[t] += 1
    
    # 토핑 순회하며 개수 비교
    for t in topping:
        left[t] += 1
        if right[t] == 1:
            del right[t]
        else:
            right[t] -= 1
        
        if len(left) == len(right):
            answer += 1
    
    return answer
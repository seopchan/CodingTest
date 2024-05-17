def solution(targets):
    targets.sort(key = lambda x:x[1])
    answer = 0
    point = -1
    
    for s, e in targets:
        if s >= point:
            answer += 1
            point = e
    
    return answer
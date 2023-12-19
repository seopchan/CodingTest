def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    answer = ''
    while True:
        p = participant.pop()
        
        if len(completion) == 0:
            answer = p
            break;
        
        c = completion.pop()
        if p != c:
            answer = p
            break
            
    return answer
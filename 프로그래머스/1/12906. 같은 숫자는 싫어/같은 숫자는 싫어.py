def solution(arr):
    answer = [arr[0]]
    pointer = 0
    
    for e in arr[1:]:
        if answer[pointer] != e:
            pointer += 1
            answer.append(e)
    
    return answer
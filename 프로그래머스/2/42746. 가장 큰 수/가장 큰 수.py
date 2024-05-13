def solution(numbers):
    numbers = sorted(map(str, numbers), key=lambda x: x*10, reverse=True)
    
    answer = ''.join(numbers)
    
    if answer[0] == '0':
        return '0'
    
    return answer
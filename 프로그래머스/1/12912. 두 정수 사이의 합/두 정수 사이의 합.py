def solution1(a, b):
    if b < a:
        a, b = b, a
    
    sum_val = 0
    for i in range(a, b+1):
        sum_val += i
        
    return sum_val

def solution(a, b):
    return (abs(a - b) + 1) * (a + b) / 2
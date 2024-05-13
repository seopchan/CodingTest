def solution(a, b):
    if b < a:
        a, b = b, a
        
    return sum(range(a, b+1))

def solution2(a, b):
    return (abs(a - b) + 1) * (a + b) / 2
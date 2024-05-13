def solution1(numbers):
    sum_val = (0 + 9) * 10 / 2
    for n in numbers:
        sum_val -= n
    
    return sum_val

def solution2(numbers):
    ls = [i for i in range(10)]
    
    for n in numbers:
        ls[n] = 0
    
    return sum(ls)

def solution(numbers):
    ls = [0] * 10
    
    for n in numbers:
        ls[n] = 1
    
    sum_val = 0
    for i, val in enumerate(ls):
        if val == 0:
            sum_val += i
            
    return sum_val
def solution(numbers):
    sum_val = (0 + 9) * 10 / 2
    for n in numbers:
        sum_val -= n
    
    return sum_val

# def solution(numbers):
#     ls = [i for i in range(10)]
    
#     for n in numbers:
#         ls[n] = 0
    
#     return sum(ls)
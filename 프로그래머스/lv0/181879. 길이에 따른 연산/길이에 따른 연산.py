from functools import reduce

def solution(num_list):
    a = 0
    
    if len(num_list) >= 11:
        a = reduce(lambda x, y: x + y, num_list)
    else:
        a = reduce(lambda x, y: x*y, num_list)
    
    return a;
    
    
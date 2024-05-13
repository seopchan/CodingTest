def solution(x):
    sum_val = 0
    for n in str(x): sum_val += int(n)
    
    if x % sum_val == 0: return True

    return False
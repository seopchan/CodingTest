def solution(absolutes, signs):
    sum_val = 0
    for i, n in enumerate(absolutes):
        if signs[i]:
            sum_val += n
        else:
            sum_val -= n
    
    return sum_val

def solution(absolutes, signs):
    sum_val = 0
    for n, sign in zip(absolutes, signs):
        if sign:
            sum_val += n
        else:
            sum_val -= n
        
    return sum_val
    
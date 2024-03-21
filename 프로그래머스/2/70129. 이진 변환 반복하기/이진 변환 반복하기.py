
def solution(s):
    count = 0
    removed_zeros = 0
    
    while s != "1":
        count += 1
        zeros = s.count('0')
        removed_zeros += zeros
        s = s.replace('0', '')
        
        s = bin(len(s))[2:]
        
    return [count, removed_zeros]
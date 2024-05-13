import math

def is_prime(x):
        if x == 1:
            return False
        
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0: return False
        return True

def solution(n, k):
    tmp = ''
    while n > 0:
        n, mod = divmod(n, k)
        tmp += str(mod)
    
    num_list = filter(lambda x: x != '', str(tmp[::-1]).split('0'))
    
    answer = 0
    for n in num_list:
        if is_prime(int(n)): answer += 1
    
    return answer


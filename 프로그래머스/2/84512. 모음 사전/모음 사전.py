from itertools import product

def solution(word):
    dic = []
    
    for i in range(1, 6):
        dic.extend([''.join(s) for s in product('AEIOU', repeat = i)])
    dic.sort()
    
    return dic.index(word) + 1
    
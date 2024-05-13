def solution(s):
    l = len(s)
    val = l // 2
    
    if l % 2 == 0:
        return s[val - 1 : val + 1]
    else:
        return s[val]
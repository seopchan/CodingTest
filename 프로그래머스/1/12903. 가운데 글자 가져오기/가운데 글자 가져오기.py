def solution(s):
    mid, is_odd = divmod(len(s), 2)
    
    return s[mid] if is_odd else s[mid-1 : mid+1]
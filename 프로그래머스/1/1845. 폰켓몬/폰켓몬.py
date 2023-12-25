def solution(nums):
    pick_len = len(nums) / 2
    set_len = len(set(nums))
    
    return min(pick_len, set_len)
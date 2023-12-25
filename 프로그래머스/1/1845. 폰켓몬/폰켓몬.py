def solution(nums):
    pick_len = len(nums) / 2
    set_len = len(set(nums))
    
    answer = pick_len if set_len > pick_len else set_len
    
    return answer
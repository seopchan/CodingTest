def solution(nums):
    count = {}
    
    for num in nums:
        if count.get(num):
            count[num] += 1
        else :
            count[num] = 1
    
    pick_count = len(nums) / 2
    
    max_kind = len(count)
    answer = min(max_kind, pick_count)
    
    return answer
    
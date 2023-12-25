def solution(clothes):
    hash_map = {}
    
    for cloth in clothes:
        cloth_type = cloth[1]
        hash_map[cloth[1]] = (hash_map[cloth_type] + 1) if cloth_type in hash_map else 2
    
    ans = 1
    for key in hash_map:
        ans *= hash_map[key]
        
    return ans - 1
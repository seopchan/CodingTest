def solution(cards):
    visited = [0] * len(cards)
    set_size_ls = []
    
    while 0 in visited:
        idx = visited.index(0) + 1
        
        s = set()
        while idx not in s:
            visited[idx - 1] = 1
            s.add(idx)
            idx = cards[idx - 1]
        set_size_ls.append(len(s))
    
    if len(set_size_ls) == 1:
        return 0
    
    set_size_ls.sort()
    return set_size_ls[-1] * set_size_ls[-2]
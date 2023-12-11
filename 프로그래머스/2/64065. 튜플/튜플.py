def solution(s):
    ss = set()
    ans = []
    
    a = s.lstrip('{').rstrip('}').split('},{')
    a.sort(key = lambda x : len(x))
    
    for l in a:
        for val in l.split(','):
            if val not in ss:
                ss.add(val)
                ans.append(int(val))
    
    return ans
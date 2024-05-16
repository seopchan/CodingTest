def solution(k, ranges):
    def calc_space(x, y):
        small = min(x, y)
        big = max(x, y)
        return big - ((big - small) / 2)
    
    seq = [k]
    n = 0
    areas = []
    while k != 1:
        n += 1
        if k % 2 == 0:
            k >>= 1
        else:
            k = k * 3 + 1
        areas.append(calc_space(seq[-1], k))
        seq.append(k)
        
    answer = []    
    for a, b in ranges:    
        if a == 0 and b == 0:
            answer.append(sum(areas))
        elif n + b < a:
            answer.append(-1)
        else:
            answer.append(sum(areas[a:n+b]))

    return answer
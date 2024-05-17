def solution(cap, n, deliveries, pickups):
    d, p = 0, 0
    answer = 0
    
    for i in range(n-1, -1, -1):
        count = 0
        # 배달
        d -= deliveries[i]
        p -= pickups[i]
        
        # 최대치만큼 왕복해야 함, 여분은 이전 집에서 처리
        while d < 0 or p < 0:
            d += cap
            p += cap
            count += 1
        
        # n번 집에 배달/최대치 왕복
        answer += (i + 1) * 2 * count
            
    return answer
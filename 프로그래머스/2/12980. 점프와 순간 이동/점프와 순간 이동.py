def solution(n):
    ans = 0
    while n > 0:
        # 점프
        if n % 2 == 1:
            n -= 1
            ans += 1
        # 순간이동
        n //= 2
        
    return ans
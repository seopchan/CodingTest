def solution(n):
    dic = {}
    pos = [0, 0]

    def task(cur, n, pos):
        if n <= 0:
            return cur

        dic[tuple(pos)] = cur
        cur += 1
        
        # 1. 아래
        for i in range(n - 1):
            pos[0] += 1
            dic[tuple(pos)] = cur
            cur += 1
        
        # 2. 오른쪽
        for i in range(n - 1):
            pos[1] += 1
            dic[tuple(pos)] = cur
            cur += 1
        
        # 3. 왼쪽 위
        for i in range(n - 2):
            pos[0] -= 1
            pos[1] -= 1
            dic[tuple(pos)] = cur
            cur += 1

        pos[0] += 1
        task(cur, n - 3, pos)

    task(1, n, pos)

    answer = [dic[(i, j)] for i in range(n) for j in range(i + 1)]
    return answer
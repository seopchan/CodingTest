def solution(n, info):
    max_diff = -1
    answer = [-1]

    def dfs(idx, arrows, lion, apeach, lion_score, apeach_score):
        nonlocal max_diff, answer
        if arrows > n:
            return
        if idx == 11:
            if arrows < n:
                lion[10] += n - arrows
            if lion_score > apeach_score:
                diff = lion_score - apeach_score
                if diff > max_diff or (diff == max_diff and lion[::-1] > answer[::-1]):
                    max_diff = diff
                    answer = lion[:]
            if arrows < n:
                lion[10] -= n - arrows
            return
        
        # 라이언이 이 점수에 대해 승리하는 경우
        if arrows + info[idx] + 1 <= n:
            lion[idx] = info[idx] + 1
            dfs(idx + 1, arrows + lion[idx], lion, apeach, lion_score + (10 - idx), apeach_score)
            lion[idx] = 0
        
        # 라이언이 이 점수에 대해 패배하는 경우
        if info[idx] > 0:
            dfs(idx + 1, arrows, lion, apeach, lion_score, apeach_score + (10 - idx))
        else:
            dfs(idx + 1, arrows, lion, apeach, lion_score, apeach_score)
    
    lion = [0] * 11
    dfs(0, 0, lion, info, 0, 0)
    
    return answer
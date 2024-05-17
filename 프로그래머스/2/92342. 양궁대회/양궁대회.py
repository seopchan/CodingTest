def solution(n, info):
    global max_diff, answer, lion
    max_diff = -1
    answer = [-1]
    lion = [0] * 11

    def dfs(score_idx, arrows, lion_score, apeach_score):
        print(10 - score_idx, arrows)
        global max_diff, answer, lion
        
        # 사용한 화살이 n보다 많으면 종료
        if arrows > n:
            return
        
        # 모든 점수 확인
        if score_idx == 11:
            # 화살이 남았으면, 남은 화살은 모두 0점
            print("hit!")
            if arrows < n:
                lion[10] += n - arrows
                
            if lion_score > apeach_score:
                diff = lion_score - apeach_score
                # 현재 점수 차가 크거나, 점수 차가 같을 때 더 낮은 점수를 많이 맞힌 경우
                if diff > max_diff or (diff == max_diff and lion[::-1] > answer[::-1]):
                    max_diff = diff
                    answer = lion[:]
                    
            # 남은 화살 복구
            if arrows < n:
                lion[10] -= n - arrows
            return
        
        # 라이언 승 -> 라이언이 어피치보다 1발 더 쏠 수 있는 경우
        if arrows + info[score_idx] + 1 <= n:
            lion[score_idx] = info[score_idx] + 1
            dfs(score_idx + 1, arrows + lion[score_idx], lion_score + (10 - score_idx), apeach_score)
            lion[score_idx] = 0
        
        # 라이언 패
        if info[score_idx] > 0:
            dfs(score_idx + 1, arrows, lion_score, apeach_score + (10 - score_idx))
        else:
            dfs(score_idx + 1, arrows, lion_score, apeach_score)
    
    dfs(0, 0, 0, 0)
    
    return answer
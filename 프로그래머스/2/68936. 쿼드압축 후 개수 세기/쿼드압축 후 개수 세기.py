from collections import deque
import math

def solution(arr):
    answer = [0, 0]
    
    def check(r, c, size):
        value = arr[r][c]
        same = True
        for i in range(r, r + size):
            for j in range(c, c + size):
                if arr[i][j] != value:
                    same = False
                    break
            if not same:
                break
        
        if same:
            answer[value] += 1
        else:
            half = size >> 1
            check(r, c, half)
            check(r, c + half, half)
            check(r + half, c, half)
            check(r + half, c + half, half)
            
        
    check(0, 0, len(arr))
    
    return answer
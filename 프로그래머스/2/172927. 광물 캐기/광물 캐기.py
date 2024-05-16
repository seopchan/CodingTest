import math

def solution(picks, minerals):
    DIA_PICK = 'dia'
    IRON_PICK = 'iron'
    STONE_PICK = 'stone'
    
    piro = {
        'diamond': {DIA_PICK: 1, IRON_PICK: 5, STONE_PICK: 25}, 
        'iron': {DIA_PICK: 1, IRON_PICK: 1, STONE_PICK: 5},
        'stone': {DIA_PICK: 1, IRON_PICK: 1, STONE_PICK: 1}
    }
    
    n = len(minerals)
    min_piro = math.inf
    
    def dfs(dia, iron, stone, mine_idx, total_piro):
        nonlocal min_piro
        if mine_idx >= n or (dia == 0 and iron == 0 and stone == 0):
            min_piro = min(min_piro, total_piro)
            return
        
        if dia > 0:
            new_piro = total_piro
            for i in range(mine_idx, min(mine_idx + 5, n)):
                new_piro += piro[minerals[i]][DIA_PICK]
            dfs(dia - 1, iron, stone, mine_idx + 5, new_piro)
        
        if iron > 0:
            new_piro = total_piro
            for i in range(mine_idx, min(mine_idx + 5, n)):
                new_piro += piro[minerals[i]][IRON_PICK]
            dfs(dia, iron - 1, stone, mine_idx + 5, new_piro)
        
        if stone > 0:
            new_piro = total_piro
            for i in range(mine_idx, min(mine_idx + 5, n)):
                new_piro += piro[minerals[i]][STONE_PICK]
            dfs(dia, iron, stone - 1, mine_idx + 5, new_piro)
    
    dfs(picks[0], picks[1], picks[2], 0, 0)
    
    return min_piro
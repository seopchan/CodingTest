import math

def solution(picks, minerals):
    DIA_PICK, IRON_PICK, STONE_PICK = 'dia', 'iron', 'stone'
    
    piro = {
        'diamond': {DIA_PICK: 1, IRON_PICK: 5, STONE_PICK: 25}, 
        'iron': {DIA_PICK: 1, IRON_PICK: 1, STONE_PICK: 5},
        'stone': {DIA_PICK: 1, IRON_PICK: 1, STONE_PICK: 1}
    }
    
    dia, iron, stone = picks
    n = len(minerals)
    min_piro = math.inf
    
    def calc_new_piro(pick_type, mine_idx, total_piro):
        new_piro = total_piro
        for i in range(mine_idx, min(mine_idx + 5, n)):
            new_piro += piro[minerals[i]][pick_type]
        return new_piro
    
    def dfs(mine_idx, total_piro):
        nonlocal min_piro, dia, iron, stone
        
        if mine_idx >= n or (dia == 0 and iron == 0 and stone == 0):
            min_piro = min(min_piro, total_piro)
            return
        
        if dia > 0:
            dia -= 1
            new_piro = calc_new_piro(DIA_PICK, mine_idx, total_piro)
            dfs(mine_idx + 5, new_piro)
            dia += 1
        
        if iron > 0:
            iron -= 1
            new_piro = calc_new_piro(IRON_PICK, mine_idx, total_piro)
            dfs(mine_idx + 5, new_piro)
            iron += 1
        
        if stone > 0:
            stone -= 1
            new_piro = calc_new_piro(STONE_PICK, mine_idx, total_piro)
            dfs(mine_idx + 5, new_piro)
            stone += 1
    
    dfs(0, 0)
    
    return min_piro
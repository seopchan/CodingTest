def solution(line):
    l = len(line)
    point = set()
    
    # 교점 찾기
    for i in range(l):
        A, B, E = line[i]
        for j in range(i + 1, l):
            C, D, F = line[j]
            
            if A * D - B * C != 0:
                x = (B * F - E * D) / (A * D - B * C)
                y = (E * C - A * F) / (A * D - B * C)
                
                # 교점이 정수 좌표인지 확인
                if x % 1 == 0 and y % 1 == 0:
                    point.add((int(x), int(y)))
    
    if not point:
        return []
    
    # 최소 크기를 위한 좌표 구하기
    min_x = min(point, key=lambda p: p[0])[0]
    min_y = min(point, key=lambda p: p[1])[1]
    max_x = max(point, key=lambda p: p[0])[0]
    max_y = max(point, key=lambda p: p[1])[1]
    
    # 행렬 초기화 (x는 열, y는 행)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    matrix = [['.' for _ in range(width)] for _ in range(height)]
    
    for x, y in point:
        matrix[max_y - y][x - min_x] = '*'
    
    result = [''.join(row) for row in matrix]
    
    return result
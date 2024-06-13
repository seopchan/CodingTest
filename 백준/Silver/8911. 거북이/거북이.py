# 8911 / 거북이

"""
(0,0) 북쪽

N -> F (0, 1) B (0, -1)
E -> F (1, 0) B (-1, 0)
S -> F (0, -1) B (0, 1)
W -> F (-1, 0) B (1, 0)

L or R -> Rotate
"""
def move(pos, direction):
    dx, dy = direction
    pos[0] += dx
    pos[1] += dy

def rotate(direction, angle):
    sumAngle = direction + angle
    if sumAngle == -90:
        return 270
    elif sumAngle == 360:
        return 0
    else:
        return sumAngle
    
def findRectangle(coords):
    minX = minY = float('inf')
    maxX = maxY = float('-inf')

    for x, y in coords:
        if x < minX: minX = x
        if y < minY: minY = y
        if x > maxX: maxX = x
        if y > maxY: maxY = y

    width, height = maxX - minX, maxY - minY
    return width, height

def main(command):
    turtle = [0, 0]
    direction = 0

    moves = {
        0: {'F': (0, 1), 'B':(0, -1) },
        90: {'F': (1, 0), 'B':(-1, 0) },
        180: {'F': (0, -1), 'B':(0, 1) },
        270: {'F': (-1, 0), 'B':(1, 0) }
    }

    area = []
    area.append(tuple(turtle))
    for c in command:
        if c in 'FB':
            move(turtle, moves[direction][c])
            area.append(tuple(turtle))
        elif c in 'LR':
            angle = -90 if c == 'L' else 90
            direction = rotate(direction, angle)

    width, height = findRectangle(area)
    print(width * height)
        
case = int(input().strip())
commands = [input().strip() for _ in range(case)]
for command in commands:
    main(command)

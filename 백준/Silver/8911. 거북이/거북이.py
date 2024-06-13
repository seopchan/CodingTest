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
    
def main(command):
    turtle = [0, 0]
    direction = 0

    moves = {
        0: {'F': (0, 1), 'B':(0, -1) },
        90: {'F': (1, 0), 'B':(-1, 0) },
        180: {'F': (0, -1), 'B':(0, 1) },
        270: {'F': (-1, 0), 'B':(1, 0) }
    }

    minX = minY = maxX = maxY = 0
    for c in command:
        if c in 'FB':
            move(turtle, moves[direction][c])
            x, y = turtle
            if x < minX: minX = x
            if y < minY: minY = y
            if x > maxX: maxX = x
            if y > maxY: maxY = y
        elif c in 'LR':
            angle = -90 if c == 'L' else 90
            direction = rotate(direction, angle)

    print((maxX - minX) * (maxY - minY))
        
case = int(input().strip())
commands = [input().strip() for _ in range(case)]
for command in commands:
    main(command)
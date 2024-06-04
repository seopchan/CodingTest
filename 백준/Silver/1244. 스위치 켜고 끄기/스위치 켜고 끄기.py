# 16303 / 스위치 켜고 끄기

# 1 ~ 연속적으로 번호가 붙어있는 스위치 
# ON / OFF

# 남 -> 스위치 번호가 자기가 받은 수의 배수이면 토글
# 여 -> N번 스위치를 중심으로 좌우 대칭, 가장 많은 스위치 포함하는 구간 토글 -> 구간은 홀수

from sys import stdin

def toggle(current):
    return '1' if current == '0' else '0'

def processMan(switchs, pos, N):
    for i in range(pos - 1, N, pos):
        switchs[i] = toggle(switchs[i])

def processWoman(switchs, pos, N):
    pos -= 1

    left = pos
    right = pos

    while left > 0 and right < N - 1 and switchs[left - 1] == switchs[right + 1]:
        left -= 1
        right += 1

    for i in range(left, right + 1):
        switchs[i] = toggle(switchs[i])

def main(N, switchs, data):
    for gender, pos in data:
        if gender == '1':
            processMan(switchs, int(pos), N)
        else:
            processWoman(switchs, int(pos), N)

    for i in range(0, N, 20):
        print(' '.join(switchs[i: i + 20]))


N = int(stdin.readline())
switchs = list(stdin.readline().strip().split())
M = int(stdin.readline())
data = [tuple(stdin.readline().split()) for _ in range(M)]

main(N, switchs, data)
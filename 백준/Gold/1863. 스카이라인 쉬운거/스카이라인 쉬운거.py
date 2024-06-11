"""
1 <= n <= 50_000

고도가 바뀌는 지점 x, y
1 <= x <= 1_000_000.0
0 <= y <= 500_000

y값이 바뀌기 전까지는 같은 빌딩
스택에 y를 넣고 바뀔 때마다 빼기
"""

import sys
input = sys.stdin.readline

def main(coords):
    stack = []
    building = 0
    for x, y in coords:
        if y and not stack:
            building += 1
            stack.append(y)
            continue

        # 고도가 낮아지면 더 높은 건물 스택에서 모두 빼기
        while stack:
            if stack[-1] > y:
                stack.pop()
            else:
                break
            
        if y and y not in stack:
            building += 1
            stack.append(y)

    print(building)
            

n = int(input())
coords = [tuple(map(int, input().strip().split())) for _ in range(n)]
main(coords)
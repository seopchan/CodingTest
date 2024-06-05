# 2493 / 탑

# N개의 높이가 서로다른 탑
# 탑은 왼쪽으로 레이저 발사

# 탐색하며 과거의 기록 확인해야 함 -> 스택

# 오른쪽의 레이저는 왼쪽에 높은 탑을 만나면 멈춤
# 스택이 있으면 최근 탑이 현재 탑의 레이저 수신 가능, 결과에 추가
# 현재 탑을 스택에 추가

from sys import stdin

def main(N, heights):
    result = [0] * N
    # (탑의 인덱스, 탑의 높이)
    stack = []

    for i in range(N):
        # 현재 탑보다 낮은 최근의 탑(레이저 수신 불가능) 제거
        while stack and stack[-1][1] < heights[i]:
            stack.pop()
        
        if stack:
            result[i] = stack[-1][0] + 1

        stack.append((i, heights[i]))

    print(' '.join(map(str, result)))

# 데이터 가져오기
N = int(stdin.readline())
heights = list(map(int, stdin.readline().split()))

main(N, heights)
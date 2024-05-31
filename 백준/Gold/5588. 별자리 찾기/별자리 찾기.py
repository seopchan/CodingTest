# 5588 / 별자리 찾기

# 모든 이동 가능한 경우의 수 확인

# 1. 별자리 2. 사진
# 1번의 별 1개를 기준점으로 설정
# 2번의 모든 별을 순회
# 기준점과 2번의 별의 차이만큼 1번을 이동

from sys import stdin

# 별자리 배열에 저장
N = int(stdin.readline())
stars = []
for _ in range(N):
    x, y = map(int, stdin.readline().split())
    stars.append((x, y))

#사진의 별 집합에 저장 -> 좌표 비교시 시간 O(1)
M = int(stdin.readline())
photoStars = set()
for _ in range(M):
    x, y = map(int, stdin.readline().split())
    photoStars.add((x, y))

# 별자리의 별 1개를 기준점으로 설정
standardX, standardY = stars[0]
# 모든 별을 옮겼을 때, 별자리와 일치하는지 확인
# 이동량은 사진의 별 - 기준점
for photoStar in photoStars:
    photoX, photoY = photoStar
    dx, dy = photoX - standardX, photoY - standardY

    allExist = True
    # 모든 별을 이동하면서 사진에 있는지 확인
    for star in stars:
        movedX, movedY = star[0] + dx, star[1] + dy
        if (movedX, movedY) not in photoStars:
            allExist = False
            break
    if allExist:
        print(dx, dy)
        break
# 게임 수 10억 -> 이분탐색
# -> X, Y는 현재 판수 -> 그러면 몇판을 더 할 수 있는지 lim를 임의로 정해야 함
def calcWinRate(x, y):
    return (y * 100) // x

def binarySearch(x, y, currentWinRate):
    left, right = 0, 10**9
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        newWinRate = calcWinRate(x + mid, y + mid)

        if newWinRate > currentWinRate:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer

def main(x, y):
    currentWinRate = calcWinRate(x, y)
    if currentWinRate >= 99:
        print(-1)
    else:
        result = binarySearch(x, y, currentWinRate)
        print(result)

x, y = map(int, input().split())
main(x, y)
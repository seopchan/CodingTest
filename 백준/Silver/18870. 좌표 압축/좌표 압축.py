# 18870 / 좌표 압축

N = int(input())
arr = list(map(int, input().strip().split()))

sortedArr = sorted(set(arr))
ziped = {n: i for i, n in enumerate(sortedArr)}

answer = [ziped[n] for n in arr]

print(' '.join(map(str, answer)))
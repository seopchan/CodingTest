# 18870 / 좌표 압축

N = int(input())
arr = list(map(int, input().strip().split()))

ziped = {n: i for i, n in enumerate(sorted(set(arr)))}
print(' '.join([str(ziped[n]) for n in arr]))
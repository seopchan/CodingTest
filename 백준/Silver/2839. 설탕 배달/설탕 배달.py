# 2839 / 설탕 배달

"""
1. N % 5 == 0인지 확인
2. N에서 5 * n//5 부터 5까지 빼면서 
    뺀 값이 3으로 나누어 떨어지는지 확인
3. N % 3 == 0인지 확인
"""
n = int(input())

def checkMix(n):
    max = n // 5
    for i in range(max, 0, -1):
        if (n - i * 5) % 3 == 0:
            return i + (n - i * 5) // 3
    return -1

mixVal = checkMix(n)
if n % 5 == 0:
    print(n//5)
elif mixVal > 0:
    print(mixVal)
elif n % 3 == 0:
    print(n // 3)
else:
    print(-1)
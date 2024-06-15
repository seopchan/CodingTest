# 11726 / 2×n 타일링

"""
피보나치 수열과 같은 규칙을 가짐
"""

def fibo(n):
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b % 10_007

def main():
    n = int(input())

    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    else:
        print(fibo(n))

main()
# 4673 / 셀프 넘버

"""
n, d(n) = 각 자리수의 합
"""

def d(n):
    return n + sum(int(digit) for digit in str(n))

def main():
    LIMIT = 10 ** 4
    hasGenerator = set()

    for i in range(1, LIMIT + 1):
        nextNum = d(i)
        if nextNum <= LIMIT:
            hasGenerator.add(nextNum)

    for i in range(1, LIMIT + 1):
        if i not in hasGenerator:
            print(i)

main()
from sys import stdin

a1, a0 = map(int, stdin.readline().strip().split())
c = int(stdin.readline().strip())
n0 = int(stdin.readline().strip())

checker = 1
for n in range(n0, 101):  # n의 범위를 100으로 제한
        if a1 * n + a0 > c * n:
            checker =  0
            break
print(checker)
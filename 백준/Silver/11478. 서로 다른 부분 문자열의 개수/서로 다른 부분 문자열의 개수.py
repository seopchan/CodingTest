# 문자열 S의 서로 다른 부분 문자열
# 경우의 수

from sys import stdin

string = stdin.readline().rstrip()

N = len(string)

answer = set()
for start in range(N):
    for end in range(start + 1, N + 1):
        answer.add(string[start:end])

print(len(answer))
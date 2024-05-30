# 1. 파일을 확장자 별로 정리, 개수 파악
# 2. 확장자들을 사전 순으로 정렬

# 딕셔너리 사용

import sys
from collections import defaultdict

N = int(sys.stdin.readline())
dic = defaultdict(int)

for _ in range(N):
    name, extension = sys.stdin.readline().strip().split('.')
    dic[extension] += 1

sortedDic = sorted(dic.items())

for extension, n in sortedDic:
    print(extension, n)
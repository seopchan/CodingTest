# 원할 때 출/퇴근
# 현재 회사에 있는 모든 사람

# 동명이인 x, 대소문자 다른 경우 다른 이름
# 딕셔너리 key -> 대소문자 구분

# 기록 백만개

import sys

N = int(sys.stdin.readline())

dic = {}
for _ in range(N):
    name, el = sys.stdin.readline().split()
    if el == "enter":
        dic[name] = True
    else:
        dic[name] = False

inCompany = []
for name, isExist in dic.items():
    if isExist:
        inCompany.append(name)
        
inCompany.sort(reverse=True)

for name in inCompany:
    print(name)
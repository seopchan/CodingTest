# 28114 / 팀명 정하기

import sys
input = sys.stdin.readline

# 입학연도 / 100 나머지 오름차순
def fn1(years):
    string = []
    for y in years:
       string.append(int(y) % 100)
    string.sort()
    return ''.join(map(str, string))

# 성씨 영문 첫글자, 해결 문제 내림차순
def fn2(students):
    dic = set()
    for p, y, n in students:
       dic.add((int(p), n))
    sortedDic = sorted(dic, reverse=True)
    string = []
    for p, n in sortedDic:
       string.append(n[0])
    return ''.join(string)

def main(students):
    print(fn1([students[0][1], students[1][1], students[2][1]]))
    print(fn2(students))

data = []
for _ in range(3):
 data.append(input().strip().split())
main(data)
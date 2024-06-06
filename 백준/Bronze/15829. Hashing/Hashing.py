# 15829 / Hashing

# 해시 함수
# 입력 : 영문 소문자
# a:1 ~ z:26

# 문자열 수열 -> 정수로 변환 -> % M

# 해시 충돌
# r: 31 M: 1234567891

from sys import stdin
r = 31
M = 1234567891

def fn(num, i):
    return num * ((r ** i))

def alphaToNum(c):
    return ord(c) - 96

def main(string):
    sum = 0
    for i, c in enumerate(string):
        num = fn(alphaToNum(c), i)
        sum += num
    
    print(sum % M)
    
L = int(stdin.readline())
string = stdin.readline().strip()
main(string)
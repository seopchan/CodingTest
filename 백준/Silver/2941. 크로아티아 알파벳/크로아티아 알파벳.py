# 2941 / 크로아티아 알파벳

# [c=, c-, dz=, d-, lj, nj, s=, z=]
# 목록에 없는 알파벳은 한 글자씩 세기
# 모든 경우의 수 작성

from sys import stdin

string = list(stdin.readline().strip())
string.reverse()

alpha = 0
i = 0
while string:
    char = string.pop()
    alpha += 1
    if string:
        if char == 'c':
            nextChar = string[-1]
            if nextChar == '=' or nextChar == '-':
                string.pop()
        elif char == 'd':
            nextChar = string[-1]
            if nextChar == '-':
                string.pop()
            elif len(string) >= 2 and nextChar == 'z':
                nextnextChar = string[-2]
                if nextnextChar == '=':
                    string.pop()
                    string.pop()
        elif char == 'l' or char == 'n':
            nextChar = string[-1]
            if nextChar == 'j':
                string.pop()
        elif char == 's' or char == 'z':
            nextChar = string[-1]
            if nextChar == '=':
                string.pop()
    
print(alpha)
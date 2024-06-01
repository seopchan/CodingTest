# 2941 / 크로아티아 알파벳

# [c=, c-, dz=, d-, lj, nj, s=, z=]
# 목록에 없는 알파벳은 한 글자씩 세기
# 모든 경우의 수 작성

from sys import stdin

string = list(stdin.readline().strip())
length = len(string)
alpha = 0
i = 0

while i < length:
    char = string[i]
    alpha += 1
    
    if i + 1 < length:
        if char == 'c' and (string[i + 1] == '=' or string[i + 1] == '-'):
            i += 1
        elif char == 'd':
            if string[i + 1] == '-':
                i += 1
            elif i + 2 < length and string[i + 1] == 'z' and string[i + 2] == '=':
                i += 2
        elif (char == 'l' or char == 'n') and string[i + 1] == 'j':
            i += 1
        elif (char == 's' or char == 'z') and string[i + 1] == '=':
            i += 1
    
    i += 1
    
print(alpha)
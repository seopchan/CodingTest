from sys import stdin
import re

def createIOString(n):
    ls = ["IO" for _ in range(n)]
    ls.append('I')
    
    return ''.join(ls)

n = int(stdin.readline())
m = int(stdin.readline())
string = stdin.readline().strip()

target = createIOString(n)
# (?=(...)) -> 긍정형 전방탐색, 패턴이 발견된 부분도 다시 확인
pattern = rf'(?=({target}))'
print(sum(1 for _ in re.findall(pattern, string)))
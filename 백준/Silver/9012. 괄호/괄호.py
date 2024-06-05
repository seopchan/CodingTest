# 9012 / 괄호

# 올바른 괄호 탐색 
# -> '('스택에 넣고 ')'이 나올 때마다 빼기
# 스택이 남거나 ')'일 때 스택 끝에 ')'가 없으면 올바르지 않음

from sys import stdin
    
case = int(stdin.readline())
psList = [stdin.readline().strip() for _ in range(case)]

vps = 0
for ps in psList:
    isVps = True
    stack = []
    for p in ps:
        if p == '(':
            stack.append(p)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                # )가 나왔는데 앞에 (가 없으면 올바르지 않음
                isVps = False
                break
    if stack:
        isVps = False

    print('YES') if isVps else print('NO')
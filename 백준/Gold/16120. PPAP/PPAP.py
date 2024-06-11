# 16120 / PPAP

"""
문자열 돌면서 각 문자를 스택에 추가
스택의 마지막 4문자가 PPAP라면 P로 변환
스택에 P만 남아있으면 PPAP 아니면 NP
"""

def main(s):
    stack = []
    for char in s:
        stack.append(char)
        if len(stack) >= 4 and stack[-4:] == ['P', 'P', 'A', 'P']:
            stack[-4:] = ['P']
    
    if stack == ['P']:
        print("PPAP")
    else:
        print("NP")

input_string = input().strip()
main(input_string)
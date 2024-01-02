def solution(s):
    stack = []
    
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            try:
                stack.pop()
            except:
                return False
            
    return len(stack) == 0
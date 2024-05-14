def solution(order):
    order_idx = 0
    size = len(order)
    
    stack = []
    current = 1
    
    while current <= size:
        if current == order[order_idx]:
            order_idx += 1
            current += 1
        else:
            if stack and stack[-1] == order[order_idx]:
                stack.pop()
                order_idx += 1
            else:
                stack.append(current)
                current += 1

        # 스택에서 순서대로 빼기
        while stack and stack[-1] == order[order_idx]:
            stack.pop()
            order_idx += 1
            
    return order_idx
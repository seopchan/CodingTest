def solution(order):
    order_idx = 0
    size = len(order)
    
    stack = []
    
    current = 1
    while current <= size:
        stack.append(current)
        current += 1
        
        while stack and stack[-1] == order[order_idx]: 
            stack.pop()
            order_idx += 1
            
    return order_idx
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            prev_index = stack.pop()
            answer[prev_index] = num
        stack.append(i)

    return answer
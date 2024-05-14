def solution(sequence, k):
    n = len(sequence)
    start, end = 0, 0
    cur_sum = sequence[0]
    min_len = 1000001
    result = []
    
    while start < n and end < n:
        if cur_sum == k:
            if (end - start) < min_len:
                min_len = end - start
                result = [start, end]
            cur_sum -= sequence[start]
            start += 1
        elif cur_sum < k:
            end += 1
            if end < n:
                cur_sum += sequence[end]
        else:
            cur_sum -= sequence[start]
            start += 1

    return result
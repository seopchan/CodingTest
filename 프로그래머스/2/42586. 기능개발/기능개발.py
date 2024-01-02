import math

def solution(progresses, speeds):
    end_dates = []
    for p, s in zip(progresses, speeds):
        end_dates.append(math.ceil((100-p) / s))
    
    answer = []
    date = end_dates[0]
    count = 0
    for ed in end_dates:
        if ed > date:
            date = ed
            answer.append(count)
            count = 1
        else:
            count += 1
    
    if count > 0:
        answer.append(count)
    
    return answer












import math
from collections import defaultdict

def solution(fees, records):
    in_records = {}
    total_time = defaultdict(int)
    
    # 주차 기록 처리
    for record in records:
        time, car_number, in_out = record.split()
        h, m = map(int, time.split(':'))
        total_min = h * 60 + m
        
        if in_out == "IN":
            in_records[car_number] = total_min
        else:
            total_time[car_number] += total_min - in_records.pop(car_number)
            
    # 출차하지 않은 차량 처리
    closing_time = 23 * 60 + 59
    for car_number, in_time in in_records.items():
        total_time[car_number] += closing_time - in_time
        
    answer = []
    for car in sorted(total_time.keys()):
        time = total_time[car]
        if time <= fees[0]: 
            fee = fees[1]
        else:
            extra_time = time - fees[0]
            fee = fees[1] + math.ceil(extra_time / fees[2]) * fees[3]
        answer.append(fee)

    return answer
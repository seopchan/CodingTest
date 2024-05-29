# 누적합?
# 각 자리수별로 계산
# 자리수 카운팅

# 'N' 까지의 모든 숫자에서 각 자릿수에서 숫자(0 ~ 9)의 등장 횟수 계산
# 각 자릿수에 대해 현재 자릿수의 숫자, 그보다 큰 숫자, 작은 숫자를 기반으로 등장 횟수 계산
# 마지막에 0횟수 조절, 다음 자릿수도 이동 후 반복
N = int(input())

count = [0] * 10

i = 1 # 자리수
while i <= N:
    lower = N - (N // i) * i 
    current = (N // i) % 10
    higher = N // (i * 10)

    for num in range(10):
        # 기본 higher * i 만큼 등장
        count[num] += higher * i
        
        if num < current: # 기준 숫자보다 작으면 자릿수만큼 등장
            count[num] += i
        elif num == current: # 기준 숫자라면 lower + 1번 등장
            count[num] += lower + 1

    # 0이 맨 앞에 오는 경우 빼기
    if i > 0:
        count[0] -= i
    
    i *= 10
 
print(' '.join(map(str, count)))
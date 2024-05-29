# 입력 데이터 -> 딕셔너리
# value로 정렬 
# 순위 계산

n, k = map(int, input().split())

data = {}
for _ in range(n):
    country, gold, silver, bronze = input().split()
    data[int(country)] = {
        'gold': int(gold),
        'silver': int(silver),
        'bronze': int(bronze)
    }

# gold -> silver -> bronze 순 내림차순 정렬
sortedData = sorted(data.items(), key=lambda item: (-item[1]['gold'], -item[1]['silver'], -item[1]['bronze']))

# 순위 계산
rankData = {}
rank = 1
prevMedals = None
for index, (country, medals) in enumerate(sortedData):
    if prevMedals is not None and medals == prevMedals:
        rankData[country] = rank
    else:
        rank = index + 1
        rankData[country] = rank
    prevMedals = medals

print(rankData[k])
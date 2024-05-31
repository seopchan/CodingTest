# 5107 / 마니또

# 사이클 찾기
# 딕셔너리에 그래프로 저장
# 방문 확인 로직으로 사이클 찾기

from sys import stdin

def findCycles(n, dic):
    visited = [False] * n # 노드 방문 확인
    nodes = list(dic.keys()) # dic의 키(노드)들을 리스트로 저장
    cycleCount = 0

    # 노드 순회
    for i in range(n):
        if not visited[i]: # 방문하지 않은 노드면
            cycleCount += 1
            current = nodes[i]
            while not visited[nodes.index(current)]:
                visited[nodes.index(current)] = True # 방문처리
                current = dic[current] # 다음 사람으로 이동

    return cycleCount

caseNum = 1
while True:
    inputLine = stdin.readline().strip()
    if inputLine == '0':
        break
    
    n = int(inputLine)
    dic = dict()
    
    for _ in range(n):
        current, next = stdin.readline().strip().split()
        dic[current] = next
    
    cycleCount = findCycles(n, dic)
    print(caseNum, cycleCount)
    caseNum += 1
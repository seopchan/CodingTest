# 최소 신장 트리(MST) -> 다익스트라, 크루스칼(탐욕법에 가까움), 프림


### 풀이 1. 크루스칼 MST 알고리즘
def find(parent, i): # 노드 i의 루트 노드 찾기
    # 자기 자신을 부모로 가지는 노드 = 루트 노드
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y): # Union-Find 알고리즘으로 Cycle형성 확인, 두 트리를 하나로 합침
    xroot = find(parent, x)
    yroot = find(parent, y)
    # 두 루트 노드의 랭크(높이)를 비교해 랭크가 낮은 트리를 랭크가 높은 트리 아래에 붙임
    if rank[xroot] < rank[yroot]:
        print(1)
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        print(2)
        parent[yroot] = xroot
    else: # 랭크가 같으면 하나를 다른 하나의 부모로 하고 해당 루트의 랭크 +1
        parent[yroot] = xroot
        print(3)
        rank[xroot] += 1
    print(parent, rank)

def solution(n, costs):
    # 간선들의 가중치 오름차순 정렬
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    rank = [0] * n
    print(costs)
    print(parent)
    print(rank)
    
    result = 0
    # 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택
    for cost in costs:
        x, y, weight = cost
        xroot = find(parent, x)
        yroot = find(parent, y)
        print("node:", x, y, "root:",xroot, yroot)
        if xroot != yroot: # 사이클을 형성하는 간선을 제외
            result += weight
            union(parent, rank, xroot, yroot)
    
    return result
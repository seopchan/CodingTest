# 1417 / 국회의원 선거

# 후보 N, 투표 M
# N <= 50, M <= 100
# 최대 득표자의 표를 빼가며 다솜 표 확인 -> 최대힙

# 다른 모든 사람의 득표수보다 많아야 함

import heapq
import sys
input = sys.stdin.readline

def main(dasom, votes):
    firstDasom = dasom
    heapq.heapify(votes) # 최대힙

    while votes and dasom <= -votes[0]:
        dasom += 1
        heapq.heapreplace(votes, votes[0] + 1)
    
    print(dasom - firstDasom)

n, dasom = int(input()), int(input())
votes = [-int(input()) for _ in range(n - 1)]
main(dasom, votes)
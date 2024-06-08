# 1417 / 국회의원 선거

# 후보 N, 투표 M
# N <= 50, M <= 100
# 최대 득표자의 표를 빼가며 

# 다른 모든 사람의 득표수보다 많아야 함

import heapq
import sys
input = sys.stdin.readline

def main(dasom, votes):
    buy = 0
    heapq.heapify(votes) # 최대힙

    while votes and dasom <= -votes[0]:
        maxVotes = -heapq.heappop(votes) - 1
        dasom += 1
        buy += 1
        heapq.heappush(votes, -maxVotes)
    
    print(buy)

n = int(input())
dasom = int(input())
votes = [-int(input()) for _ in range(n - 1)]
main(dasom, votes)
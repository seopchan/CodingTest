# 매번 정렬
import heapq
import sys
input = sys.stdin.readline

def main(dasom, votes):
    buy = 0
    votes.sort(reverse=True)

    while votes and dasom <= votes[0]:
        dasom += 1
        votes[0] -= 1
        buy += 1
        
        votes.sort(reverse=True)
    
    print(buy)

n = int(input())
dasom = int(input())
votes = [int(input()) for _ in range(n - 1)]
main(dasom, votes)
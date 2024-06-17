# 1713 / 후보 추천하기

"""
1. 사진틀 n개
2. 추천받으면 사진틀에 게시
3. 빈 사진틀이 없으면 최소 추천 학생 삭제
    동률이면 더 오래된 사진 삭제 -> heapq 사용

-> 추천 개수도 관리해야함 -> heapq로는 안 됨

단순 구현해야 할듯
"""
def addPicturesWithRecommends(n, m, recommends):
    사진 = {} # {학생 번호: 추천 횟수}
    게시순서 = [] # [학생 번호]

    for student in recommends:
        if student in 사진:
            # 이미 사진이 올라가 있으면 추천 +1
            사진[student] += 1
        else:
            if len(사진) < n:
                # 사진이 비었으면 넣기
                사진[student] = 1
                게시순서.append(student)
            else:
                # 사진이 다 찼으면, 최소 추천 학생 제거
                minRecommend = min(사진.values())
                # 최소 추천 개수 학생 중 가장 오래된 학생 제거
                for s in 게시순서:
                    if 사진[s] == minRecommend:
                        게시순서.remove(s)
                        del 사진[s]
                        break
                # 새 사진 추가
                사진[student] = 1
                게시순서.append(student)

    return(' '.join(map(str, sorted(사진.keys()))))

def main():
    n = int(input())
    m = int(input())
    recommends = list(map(int, input().strip().split()))
    print(addPicturesWithRecommends(n, m, recommends))

main()
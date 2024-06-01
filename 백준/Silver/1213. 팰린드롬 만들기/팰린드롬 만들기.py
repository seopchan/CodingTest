# 1213 / 팰린드롬 만들기
# 팰린드롬 (기러기, 토마토)

# 짝수, 홀수 계산
# 모두 짝수 or 1개만 홀수

from sys import stdin

ALPHA = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
alphaToIndex = {c: i for i, c in enumerate(ALPHA)}
indexToAlpha = {i: c for i, c in enumerate(ALPHA)}

def makePalHalf(countAlpha):
    ls = []
    for i, count in enumerate(countAlpha):
        alpha = indexToAlpha[i]
        ls.append(alpha * (count // 2))
    return ''.join(ls)

def main():
    name = stdin.readline().strip()
    
    countAlpha = [0] * 26
    for char in name: countAlpha[alphaToIndex[char]] += 1

    oddCount, oddAlpha = 0, ''

    # 홀수 개수의 알파벳 체크
    for i, count in enumerate(countAlpha):
        if count % 2:
            # 홀수가 여러 개면 팰린드롬을 만들 수 없음
            if oddCount:
                print("I'm Sorry Hansoo")
                return
            oddCount += 1
            oddAlpha = indexToAlpha[i]

    # 앞의 절반과 뒤의 절반을 위한 문자열 생성
    halfPal = makePalHalf(countAlpha)

    answer = []
    # 앞의 절반
    answer.append(halfPal)
    
    # 홀수 개의 알파벳이 있으면 중간에 추가
    if oddAlpha: answer.append(oddAlpha)

    # 뒤의 절반 (앞의 절반을 뒤집어서 추가)
    answer.append(halfPal[::-1])

    print(''.join(answer))

main()
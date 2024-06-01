from sys import stdin

def countIoIPatterns(string, n):
    pattern_count = 0  # 현재 IOI 패턴이 몇 번 반복되었는지 카운트
    pattern_counts = []  # 패턴 카운트를 저장할 리스트
    i = 0

    while i < len(string) - 1:
        # IOI 패턴을 찾기
        if string[i:i + 3] == "IOI":
            pattern_count += 1
            i += 2  # IOI가 겹치므로 2만큼 이동
        else:
            # 패턴이 끊기면 현재 pattern_count를 리스트에 추가
            if pattern_count > 0:
                pattern_counts.append(pattern_count)
                pattern_count = 0  # 패턴이 끊기면 초기화
            i += 1

    # 마지막으로 남아있는 패턴 카운트를 리스트에 추가
    if pattern_count > 0:
        pattern_counts.append(pattern_count)

    return pattern_counts

# 표준 입력에서 읽어오기
n = int(stdin.readline().strip())
m = int(stdin.readline().strip())
string = stdin.readline().strip()

pattern_counts = countIoIPatterns(string, n)
answer = 0
for count in pattern_counts:
    if count >= n:
        answer += count - n + 1
print(answer)
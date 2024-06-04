# 3107 / IPv6

# IPv6 128비트
# 32자리의 16진수를 4자리씩 끊기

# 1. 0의 전체 또는 일부 생략
# 0db8 -> db8
# 0000 -> 0
# 0000 -> 00

# 2. 0으로만 이루어져있는 그룹이 있을 때, 한 개 이상 연속된 그룹 ::으로 바꾸기
# :0000:0000: -> ::
# 2번은 1번만 사용 가능

from sys import stdin
TOTAL_SIZE = 8
SUB_SIZE = 4

def restore0(val):
    length = len(val)
    need0 = SUB_SIZE - length
    return '0' * need0 + val

# ::안에 몇개의 0그룹이 들어있는지 찾기
def restore0Groups(length):
    need0Group = TOTAL_SIZE - length
    return ['0000'] * need0Group

def main(ip):
    restoredIP = []
    length = len(ip)

    nullCount = ip.count('')

    if nullCount == 3:
        print(':'.join(restore0Groups(0)))
        

    hasDoubleColon = False
    for val in ip:
        if val:
            if len(val) == 4: # 1. 글자가 4자리면 정상
                restoredIP.append(val)
            else: # 2. 글자가 4보다 작으면 생략됨
                restoredIP.append(restore0(val))
        else: # 3. :: 찾기 -> restore0Groups
            if nullCount == 1 or (nullCount == 2 and hasDoubleColon):
                restoredIP.extend(restore0Groups(length - nullCount))

            if nullCount == 2 and not hasDoubleColon:
                hasDoubleColon = True
    
    print(':'.join(restoredIP))

ip = stdin.readline().strip().split(':')
main(ip)

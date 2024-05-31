# 25192 / 인사성 밝은 곰곰이

# 입장 -> 곰곰티콘
# set을 사용해 새로운 입장 후 첫 채팅인지 확인

from sys import stdin

n = int(stdin.readline())
alreadyChat = set()
gomgomCount = 0

for _ in range(n):
    log = stdin.readline().strip()

    if log == "ENTER":
        alreadyChat.clear()
    else:
        if log not in alreadyChat:
            gomgomCount += 1
            alreadyChat.add(log)
            
print(gomgomCount)
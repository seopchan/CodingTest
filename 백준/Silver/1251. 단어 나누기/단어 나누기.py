# 1251 / 단어 나누기

"""
단어를 임의의 세 부분으로 나눈다 -> reverse -> join
"""

def main(string):
    l = len(string)
    answer = []
    for i in range(1, l - 1):
        for j in range(i + 1, l):
            newStr = []
            newStr.extend(reversed(string[:i]))
            newStr.extend(reversed(string[i:j]))
            newStr.extend(reversed(string[j:]))
            answer.append(''.join(newStr))
    answer.sort()
    print(answer[0])

string = input().strip()
main(string)
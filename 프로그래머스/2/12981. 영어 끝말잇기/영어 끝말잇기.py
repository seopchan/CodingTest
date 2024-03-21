def solution(n, words):
    used_words = set()
    last_char = words[0][0]

    for i, word in enumerate(words):
        # 현재 단어의 첫 글자가 이전 단어의 마지막 글자와 다르거나, 이미 사용된 단어인 경우
        if word in used_words or last_char != word[0]:
            # 탈락자 번호와 차례를 계산하여 반환
            return [(i % n) + 1, (i // n) + 1]
        used_words.add(word)  # 현재 단어를 사용된 단어 집합에 추가
        last_char = word[-1]  # 마지막 글자를 업데이트

    return [0, 0]
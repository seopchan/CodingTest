def solution(phone_book):
    trie = {}
    for phone_number in phone_book:
        current_node = trie
        for number in phone_number:
            if number not in current_node:
                current_node[number] = {}
            current_node = current_node[number]
            if "end" in current_node:
                return False
        current_node["end"] = True

        # 다른 번호가 현재 번호의 접두사인지 확인
        if len(current_node) > 1:
            return False
    return True
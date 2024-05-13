def solution(numbers):
    answer = []
    for x in numbers:
        if x % 2 == 0:
            # 짝수인 경우 + 1
            answer.append(x + 1)
        else:
            # 홀수인 경우
            bin_x = list(bin(x)[2:])
            
            # 뒤에서 첫 번째 '0' 찾기
            for i in range(len(bin_x) - 1, -1, -1):
                if bin_x[i] == '0':
                    bin_x[i] = '1'  # '0'을 '1'로 변경
                    bin_x[i + 1] = '0'  # 그 다음 비트를 '0'으로 변경
                    break
            else:
                # 모든 비트가 '1'인 경우, 앞에 10 추가, 원본의 1번 인덱스부터 붙임
                bin_x = ['1', '0'] + bin_x[1:]
            
            answer.append(int(''.join(bin_x), 2))
    
    return answer

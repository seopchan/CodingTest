def solution(s):
    dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    text = ''
    for c in s:
        if c.isalpha():
            text += c
            
            if dict.get(text):
                print(text)
                s = s.replace(text, dict[text])
                text = ''
                print(s)
                
    return int(s)
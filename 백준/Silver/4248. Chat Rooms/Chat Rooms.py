VOWELS = "aeiouyAEIOUY"
CONSONANTS = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

N = int(input().strip())
answers = ['y\n'] * N
check4Result = [False] * N
chats = [""] * N
for i in range(N):
    chats[i] = input()

def check5(line):
    count = 0
    for c in line:
        if c in CONSONANTS:
            count += 1
            if count > 5:
                return True
        else:
            count = 0
    return False

def check4(line, index):
    words = line.split()
    count = 0

    for word in words:
        for c in word:
            if c in CONSONANTS:
                count += 1
                if count > 4:
                    check4Result[index] = True
                    break
            else:
                count = 0
    
    if check4Result[index] and check4Result[max(0, index - 10) : index].count(True) > 2:
        return True 
    else:
        return False
    
def checkTwice(line, index):
    if chats[max(0, index - 10):index].count(line) > 1: return True
    else: return False

for i, line in enumerate(chats):
    if check5(line):
        answers[i] = 'n\n'
        continue

    if check4(line, i):
        answers[i] = 'n\n'

    if checkTwice(line, i):
        answers[i] = 'n\n'

print(''.join(answers))
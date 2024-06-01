import sys

sentence = sys.stdin.readline().strip()
cnt, idx = 0, 0
two = {'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z='}  # Changed to a set
three = 'dz='

while idx < len(sentence):
    if sentence[idx:idx+3] == three:
        idx += 3
    elif sentence[idx:idx+2] in two:
        idx += 2
    else:
        idx += 1
    cnt += 1

print(cnt)
import sys

A = []
QLen = int(sys.stdin.readline())
removed = []

for _ in range(QLen):
    data = sys.stdin.readline().split()
    if data[0] == '1':
        A.append(int(data[1]))
    else:
        mid = len(A) // 2

        sumLeft = sum(A[:mid])
        sumRight = sum(A[mid:])

        if sumLeft > sumRight:
            removed.append(sumRight)
            A = A[:mid]
        else:
            removed.append(sumLeft)
            A = A[mid:]

for val in removed:
    print(val)
print(' '.join(map(str, A)))

import sys

A = []

def f1(x):
    A.append(x)

def f2(mid):
    global A

    frontSum = sum(A[:mid])
    backSum = sum(A[mid:])

    if frontSum <= backSum:
        A = A[mid:]
        print(frontSum)
    elif frontSum > backSum:
        A = A[:mid]
        print(backSum)

N = int(sys.stdin.readline())
for _ in range(N):
    data = sys.stdin.readline().split()

    if data[0] == '1':
        f1(int(data[1]))
    else:
        f2(len(A) // 2)

print(' '.join(map(str, A)))
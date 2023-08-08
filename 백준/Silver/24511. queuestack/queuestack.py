import sys
from collections import deque

# 기본 변수 입력 받기
N = int(sys.stdin.readline())
A = deque(list(map(int, sys.stdin.readline().split())))
B = deque(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
C = deque(list(map(int, sys.stdin.readline().split())))

deq = deque()
for i in range(N):
    if A[i] == 0:
        deq.append(B[i])

if len(deq) == 0:
    print(*C)
else:
    for i in range(M):
        print(deq.pop(), end=' ')
        deq.appendleft(C[i])
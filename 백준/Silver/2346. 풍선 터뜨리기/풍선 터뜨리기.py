import sys
from collections import deque

# 기본 변수 입력 받기
N = int(sys.stdin.readline())
arr = deque(list(range(1, N + 1)))
# 덱 리스트 생성
deq = deque(list(map(int, sys.stdin.readline().split())))

# 풍선이 다 터질때까지 진행
while len(arr) != 0:
    print(arr[0], end=' ')
    A = deq.popleft()
    arr.popleft()
    if A > 0:
        deq.rotate(- A + 1)
        arr.rotate(- A + 1)
    else:
        deq.rotate(- A)
        arr.rotate(- A)
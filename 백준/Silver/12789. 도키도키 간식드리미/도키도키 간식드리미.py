import sys
from collections import deque

# 학생의 수와 대기 줄 입력 받기
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 데크 생성
deq = deque()
arr = deque(arr)
# 간식을 다 받거나 더 이상 받을 수 없을때까지 시행
while True:
    # 사람이 모두 나갔으면 탈출
    if len(arr) + len(deq) == 0:
        print('Nice')
        exit()

    # deq 공간에 사람이 있다면
    while True:
        if len(deq) == 0:
            break
        # 바로 들어갈 수 있는 경우 대기 줄에서 제거
        if deq[-1] == N + 1 - len(arr) - len(deq):
            deq.pop()
        # 대기 줄에 사람이 없고, 더 이상 들어갈 수 있는 사람이 없으면
        elif deq[-1] != N + 1 - len(arr) - len(deq) and len(arr) == 0:
            print('Sad')
            exit()
        else:
            break

    # 대기 줄에 사람이 있다면
    if len(arr) != 0:
        # 바로 들어갈 수 있는 경우 대기 줄에서 제거
        if arr[0] == N + 1 - len(arr) - len(deq):
            arr.popleft()
        # 들어갈 수 있는 차례가 아닌 경우 데크에 삽입
        else:
            deq.append(arr[0])
            arr.popleft()
import sys
from collections import deque

# 자연수 입력 받기
T = int(sys.stdin.readline())

for i in range(1, T + 1):
    M, N = map(int, sys.stdin.readline().split())
    importance = list(map(int, sys.stdin.readline().split()))
    deq = deque(importance)
    stack = []
    while True:
        # 중요도 궁금한 문서가 맨 앞에 온 경우
        if N == 0:
            # 남은 문서 중 제일 중요한 경우
            if deq[0] == max(deq):
                print(len(stack) + 1)
                break
            # 뒤에 더 중요한 문서가 있는 경우
            else:
                deq.rotate(-1)
                N += len(deq) - 1
        # 그 외의 문서
        else:
            # 남은 문서 중 제일 중요한 경우
            if deq[0] == max(deq):
                stack.append(deq.popleft())
                N -= 1
            # 뒤에 더 중요한 문서가 있는 경우
            else:
                deq.rotate(-1)
                N -= 1

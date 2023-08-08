import sys
from collections import deque

# 명령의 수 입력 받기
N = int(sys.stdin.readline())

# 큐 리스트 생성
que = deque()

# N개 만큼의 명령 입력 받기
for i in range(N):
    order = sys.stdin.readline().split()

    # 명령어가 push 인 경우 정수를 스택에 넣는다
    if order[0] == 'push':
        que.append(int(order[1]))
    # 명령어가 push 가 아닌 경우
    else:
        if order[0] == 'pop':
            if len(que) != 0:
                print(que.popleft())
            else:
                print(-1)
        elif order[0] == 'size':
            print(len(que))
        elif order[0] == 'empty':
            if len(que) != 0:
                print(0)
            else:
                print(1)
        elif order[0] == 'front':
            if len(que) != 0:
                print(que[0])
            else:
                print(-1)
        elif order[0] == 'back':
            if len(que) != 0:
                print(que[-1])
            else:
                print(-1)
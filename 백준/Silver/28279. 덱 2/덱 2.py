import sys
from collections import deque

# 명령의 수 입력 받기
N = int(sys.stdin.readline())

# 덱 리스트 생성
deq = deque()

# N개 만큼의 명령 입력 받기
for i in range(N):
    order = sys.stdin.readline().split()

    # 명령어가 1, 2 인 경우 정수를 덱에 넣는다
    if order[0] == '1':
        deq.appendleft(int(order[1]))
    elif order[0] == '2':
        deq.append(int(order[1]))
    # 명령어가 1, 2 가 아닌 경우
    else:
        if order[0] == '3':
            if len(deq) != 0:
                print(deq.popleft())
            else:
                print(-1)
        elif order[0] == '4':
            if len(deq) != 0:
                print(deq.pop())
            else:
                print(-1)
        elif order[0] == '5':
            print(len(deq))
        elif order[0] == '6':
            if len(deq) != 0:
                print(0)
            else:
                print(1)
        elif order[0] == '7':
            if len(deq) != 0:
                print(deq[0])
            else:
                print(-1)
        elif order[0] == '8':
            if len(deq) != 0:
                print(deq[-1])
            else:
                print(-1)
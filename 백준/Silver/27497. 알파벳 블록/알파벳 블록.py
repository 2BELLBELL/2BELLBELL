import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
alp_stack = deque()
num_stack = deque()

for i in range(N):
    order = sys.stdin.readline().split()
    # 1번이 들어오면 숫자리스트에 1 추가
    # 영어리스트 맨뒤에 해당 알파벳 추가
    if order[0] == '1':
        alp_stack.append(order[1])
        num_stack.append(order[0])
    # 2번이 들어오면 숫자리스트에 2 추가
    # 영어리스트 맨앞에 해당 알파벳 추가
    elif order[0] == '2':
        alp_stack.appendleft(order[1])
        num_stack.append(order[0])
    # 3이 들어왔따
    else:
        # 알파벳이 비어있지 않으면
        if len(alp_stack) != 0:
            # 마지막 추가된 숫자 확인
            # 1이면
            if num_stack[-1] == '1':
                alp_stack.pop()
                num_stack.pop()
            else:
                alp_stack.popleft()
                num_stack.pop()

if len(alp_stack) == 0:
    print(0)
else:
    print(''.join(alp_stack))
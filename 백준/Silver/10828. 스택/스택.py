import sys

N = int(sys.stdin.readline())
stack = []
for i in range(1, N + 1):
    order = list(sys.stdin.readline().split())
    # push의 경우
    if len(order) == 2:
        X = int(order[1])
        # 스택에 정수 X를 넣는다
        stack.append(X)
    else:
        # pop의 경우
        if order == ['pop']:
            # 스택이 비어 있는 경우
            if len(stack) == 0:
                print('-1')
            # 스택에 정수가 있는 경우
            else:
                print(stack.pop())
        # top의 경우
        elif order == ['top']:
            # 스택이 비어 있는 경우
            if len(stack) == 0:
                print('-1')
            # 스택에 정수가 있는 경우
            else:
                print(stack[-1])
        # size의 경우
        elif order == ['size']:
            print(len(stack))
        # empty의 경우
        elif order == ['empty']:
            # 스택이 비어 있는 경우
            if len(stack) == 0:
                print('1')
            # 스택에 정수가 있는 경우
            else:
                print('0')
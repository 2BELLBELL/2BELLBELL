import sys

# 명령의 수 입력 받기
N = int(sys.stdin.readline())

# 스택 리스트 생성
stack = []

# N개 만큼의 명령 입력 받기
for i in range(N):
    order = sys.stdin.readline().split()

    # 명령어가 1 로 시작하면 정수를 스택에 넣는다
    if order[0] == '1':
        stack.append(int(order[1]))
    # 명령어가 1 이 아닌 경우
    else:
        if order[0] == '2':
            if len(stack) != 0:
                print(stack.pop())
            else:
                print(-1)
        elif order[0] == '3':
            print(len(stack))
        elif order[0] == '4':
            if len(stack) != 0:
                print(0)
            else:
                print(1)
        elif order[0] == '5':
            if len(stack) != 0:
                print(stack[-1])
            else:
                print(-1)

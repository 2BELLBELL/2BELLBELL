import sys

K = int(sys.stdin.readline())
stack = []

# K만큼 한줄씩 실행
for i in range(1, K + 1):
    number = int(sys.stdin.readline())
    # 0이 아닌 수가 들어오면 스택에 추가
    if number != 0:
        stack.append(number)
    # 0이 들어오면 스택에 가장 최근 값 삭제
    elif number == 0:
        stack.pop()

# 스택의 합
print(sum(stack))
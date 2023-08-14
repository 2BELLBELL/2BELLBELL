import sys

N = int(sys.stdin.readline().rstrip())
stack = []
score = 0

for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    if len(a) == 1:
        pass
    else:
        stack.append([a[1], a[2]])

    # 스택이 비어있는게 아니면 과제 시작
    if len(stack) != 0:
        stack[-1][-1] -= 1
        # 과제가 끝났다면 점수 획득 후 과제 치우기
        if stack[-1][-1] == 0:
            score += stack[-1][0]
            stack.pop()

print(score)
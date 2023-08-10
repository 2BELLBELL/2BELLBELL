import sys

N = int(sys.stdin.readline())
cnt = 0

for _ in range(N):
    # 단어를 입력 받는다
    word = sys.stdin.readline().strip()
    stack = []
    for i in word:
        # 스택이 비어있으면 일단 넣어라
        if len(stack) == 0:
            stack.append(i)
        # 스택에 알파벳이 있으면 검사 해봅시다
        else:
            # 전에꺼하고 같으면 없애고 같으면 넣는다
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    # 스택이 비게되면 좋은 단어 카운팅
    if len(stack) == 0:
        cnt += 1

print(cnt)
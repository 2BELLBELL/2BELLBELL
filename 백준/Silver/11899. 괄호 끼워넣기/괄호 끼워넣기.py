import sys

arr = sys.stdin.readline().rstrip()
stack = []

for i in arr:
    # 스택이 비어있으면 무조건 넣는다
    if len(stack) == 0:
        stack.append(i)
    # 스택이 하나라도 있는 경우
    else:
        # 여는 괄호면 넣는다
        if i == '(':
            stack.append(i)
        # 닫는 괄호면 비교 후 넣거나 pop
        else:
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)

# 남은 짝이 없는 스택
print(len(stack))
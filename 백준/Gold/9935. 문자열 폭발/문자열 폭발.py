from collections import deque

word = input()
bomb = input()
stack = deque()

# word 에서 글자를 한개씩 스택에 삽입한다
for i in word:
    stack.append(i)
    # 스택의 마지막 글자와 폭발 문자열의 마지막 글자가 같으면 검사 실행
    if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
        flag = True
        for j in range(2, len(bomb) + 1):
            if stack[-j] != bomb[-j]:
                flag = False
        # 모든 문자열이 일치하면 폭발 문자열의 수만큼 pop
        if flag:
            for k in range(len(bomb)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
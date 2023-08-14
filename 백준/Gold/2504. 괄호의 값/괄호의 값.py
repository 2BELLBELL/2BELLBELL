import sys

arr = sys.stdin.readline().rstrip()
stack = []
try:
    for i in arr:
        # 스택이 비어있으면 무조건 넣는다
        if len(stack) == 0:
            stack.append(i)
        # 스택이 하나라도 있는 경우
        else:
            # 여는 괄호면 넣는다
            if i == '(' or i == '[':
                stack.append(i)
            # 닫는 소괄호면
            elif i == ')':
                lst = 0
                # 여는 소괄호가 나올 때까지
                while True:
                    if stack[-1] == '(':
                        if lst == 0:
                            stack.pop()
                            stack.append(2)
                            break
                        else:
                            stack.pop()
                            stack.append(lst*2)
                            break
                    else:
                        lst += stack.pop()
            # 닫는 대괄호면
            elif i == ']':
                lst = 0
                # 여는 대괄호가 나올 때까지
                while True:
                    if stack[-1] == '[':
                        if lst == 0:
                            stack.pop()
                            stack.append(3)
                            break
                        else:
                            stack.pop()
                            stack.append(lst*3)
                            break
                    else:
                        lst += stack.pop()
    print(sum(stack))

except:
    print(0)

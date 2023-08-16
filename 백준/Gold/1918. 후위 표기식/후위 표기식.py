# 후위 표기식으로 변환할 함수
def change(arr):
    ans = ''
    stack = []
    for i in arr:
        # 숫자면 ans 에 넣는다
        if i.isalpha():
            ans += i
        else:
            # 여는 괄호는 바로 삽입
            if i == '(':
                stack.append(i)
            # 곱하기, 나누기는 스택이 비거나 곱하기 or 나누기가 나올때까지 pop
            elif i == '*' or i == '/':
                while len(stack) > 0 and (stack[-1] == '*' or stack[-1] == '/'):
                    ans += stack.pop()
                # 스택에 연산자 삽입
                stack.append(i)
            # 플러스나 마이너스는 스택이 비거나 여는 괄호가 나올때까지 pop
            elif i == '+' or i == '-':
                while len(stack) > 0 and stack[-1] != '(':
                    ans += stack.pop()
                # 스택에 연산자 삽입
                stack.append(i)
            # 닫는 괄호가 나오면 여는 괄호 나올때까지 pop
            else:
                while len(stack) > 0 and stack[-1] != '(':
                    ans += stack.pop()
                # 여는 괄호도 pop
                stack.pop()

    # 남은 스택의 연산자를 ans 에 pop 한다
    while stack:
        ans += stack.pop()
    # ans 반환
    return ans

arr = list(input())
change_arr = change(arr)
print(change_arr)
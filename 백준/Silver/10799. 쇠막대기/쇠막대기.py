arr = input()

# 레이저 눈에 띄게 바꾸기
arr = list(arr.replace('()', 'L'))

# 쇠 막대 개수
stick = 0
# 현재 막대 개수
cnt = 0

# 모든 배열 선회
for i in arr:
    # 여는 괄호 들어오면
    if i == '(':
        cnt += 1
        stick += 1

    # 레이저 들어오면
    elif i == 'L':
        stick += cnt

    # 닫는 괄호가 들어오면
    elif i == ')':
        cnt -= 1

# 쇠막대 개수 출력
print(stick)
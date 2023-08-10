import sys
from collections import deque

n = int(sys.stdin.readline().strip())

# 완성된 임의의 수열
seq = deque()
for i in range(n):
    seq.append(int(sys.stdin.readline().strip()))

# 1부터 n 까지의 수열
arr = deque(list(range(1, n + 1)))
# 스택을 넣을 리스트
stack = deque()
# 출력용 +, - 를 넣을 리스트
result = []

while True:
    # 모든 숫자가 일치하면
    if len(seq) == 0:
        break
    # 스택이 비어있으면 무조건 넣는다
    if len(stack) == 0 and len(arr) != 0:
        stack.append(arr.popleft())
        result.append('+')
    # arr 가 비어 있고 들어 갈 수 있는 숫자가 없으면
    if len(arr) == 0 and stack[-1] != seq[0]:
        print('NO')
        exit()
    # top 에 연속으로 들어갈 수 있으면 반복해야함
    while True:
        if len(stack) != 0:
            # 스택의 top 과 들어가야하는 숫자가 동일한 경우
            if stack[-1] == seq[0]:
                stack.pop()
                seq.popleft()
                result.append('-')
            # 스택의 top 과 들어가야하는 숫자가 다른 경우
            else:
                if len(arr) != 0:
                    stack.append(arr.popleft())
                    result.append('+')
                    break
                else:
                    break
        else:
            break

for i in result:
    print(i)
from collections import deque

N, K = map(int, input().split())

arr = deque(list(range(1, N + 1)))
result = deque()

# arr 가 빈 배열이 될때까지 반복
while True:
    # arr 가 비었으면 반복 중지
    if len(arr) == 0:
        break
    # K - 1번 회전
    for i in range(K-1):
        arr.append(arr.popleft())
    # arr에서 제거하며 result 에 삽입
    else:
        result.append(arr.popleft())

print('<', end='')
print(*result, sep=', ', end='')
print('>')
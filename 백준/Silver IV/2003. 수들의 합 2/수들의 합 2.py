N, M = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
left = 0
right = left + 1

while right <= N and left <= right:
    total = sum(arr[left:right])
    if total == M:
        cnt += 1
        left += 1
        right = left + 1
    if total < M:
        right += 1
    if total > M:
        left += 1
        right = left + 1

print(cnt)
import sys
T = int(input())

# 좌표 오름차순 정렬
arr = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(T)])

cnt = 0
max_high = 0
max_idx = 0

# 최고 높이와 인덱스 구하기
for i in range(len(arr)):
    if arr[i][1] > max_high:
        max_high = arr[i][1]
        max_idx = i

# 최고 기둥 높이 기준으로 나누기
arr_left = arr[:max_idx+1]
arr_right = list(reversed(arr[max_idx:]))

high = 0
# 최고 높이 전까지는 high 갱신하면서 더해주기
for i in range(len(arr_left) - 1):
    if arr_left[i][1] > high:
        high = arr_left[i][1]
    cnt += high * (arr_left[i+1][0] - arr_left[i][0])

high = 0
# 역순으로 똑같이
for i in range(len(arr_right) - 1):
    if arr_right[i][1] > high:
        high = arr_right[i][1]
    cnt += high * (arr_right[i][0] - arr_right[i+1][0])
# 최고 높이는 따로 더해준다
cnt += max_high

print(cnt)
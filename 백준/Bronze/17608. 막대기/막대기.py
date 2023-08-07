import sys
N = int(sys.stdin.readline())
arr = []

# 입력 값을 arr에 삽입한다
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

# 최고 높이와 카운트를 마지막 막대 기준으로 세팅
high = arr[-1]
cnt = 1

# arr를 역으로 선회한다
for i in range(N - 1, -1, -1):
    # 최고 막대보다 높은게 나오면 막대 교체 후 cnt + 1
    if arr[i] > high:
        high = arr[i]
        cnt += 1

print(cnt)
import sys

N, K = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

for i in range(N - 1, 0, -1):
    max_idx = i
    for j in range(i):
        if arr[max_idx] < arr[j]:
            max_idx = j

    if arr[i] != arr[max_idx]:
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        K -= 1

    if K == 0:
        print(arr[max_idx], arr[i])
        exit()

print(-1)
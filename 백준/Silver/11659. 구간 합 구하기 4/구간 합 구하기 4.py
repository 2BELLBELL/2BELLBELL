import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0] * (N + 1)

for i in range(1, N + 1):
    if i == 1:
        sum_arr[i] = arr[i - 1]
    else:
        sum_arr[i] = (arr[i - 1] + sum_arr[i - 1])

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_arr[j] - sum_arr[i - 1])
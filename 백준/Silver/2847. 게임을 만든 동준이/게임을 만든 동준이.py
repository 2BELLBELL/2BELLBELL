N = int(input())
arr = []
cnt = 0
for i in range(N):
    arr.append(int(input()))
top = arr[N - 1]

for i in range(N - 2, -1, -1):
    if arr[i] >= arr[i+1]:
        cnt += arr[i] - (arr[i+1] - 1)
        arr[i] = arr[i+1] - 1

print(cnt)
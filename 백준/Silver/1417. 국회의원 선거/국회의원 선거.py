N = int(input())
dasom = int(input())
arr = [int(input()) for _ in range(N - 1)]
cnt = 0
if arr:
    while dasom <= max(arr):
        arr[arr.index(max(arr))] -= 1
        dasom += 1
        cnt += 1

print(cnt)
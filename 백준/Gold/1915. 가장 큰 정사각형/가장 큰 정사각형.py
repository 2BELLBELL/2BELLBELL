n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

cnt = 0

for i in range(n):
    for j in range(m):
        if i > 0 and j > 0 and arr[i][j] == 1:
            arr[i][j] += min(arr[i][j-1], arr[i-1][j], arr[i-1][j-1])
        cnt = max(cnt, arr[i][j])
print(cnt * cnt)
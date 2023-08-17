def dfs(x, y):
    global total
    total += 1
    arr[x][y] = 0

    for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nx = x+i
        ny = y+j
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
            dfs(nx, ny)



N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
cnt = 0
stack = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            total = 0
            dfs(i, j)
            cnt += 1
            stack.append(total)

print(cnt)
stack.sort()

for i in stack:
    print(i)
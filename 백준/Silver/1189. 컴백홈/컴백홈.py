def dfs(x, y):
    if x == end[0] and y == end[1] and visited[x][y] == K:
        global answer
        answer += 1
        return

    for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        nx, ny = x + i, y + j
        if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == False and arr[nx][ny] != 'T':
            visited[nx][ny] = visited[x][y] + 1
            dfs(nx, ny)
            visited[nx][ny] = False

R, C, K = map(int, input().split())
arr = [input() for _ in range(R)]
visited = [[False] * C for _ in range(R)]
answer = 0
start = (R - 1, 0)
end = (0, C - 1)
visited[start[0]][start[1]] = 1
dfs(start[0], start[1])
print(answer)
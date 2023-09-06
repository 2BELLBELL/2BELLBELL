N, M, K = map(int, input().split())
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

if K % M != 0:
    tmp = (K // M, K % M - 1)
else:
    tmp = ((K // M) - 1, M - 1)


for i in range(N):
    for j in range(M):
        if i == j == 0:
            continue
        if tmp[0] < i and tmp[1] > j:
            continue
        elif tmp[0] > i and tmp[1] < j:
            continue
        else:
            nx, ny = i - 1, j - 1
            if 0 > nx:
                visited[i][j] = visited[i][ny]
            elif 0 > ny:
                visited[i][j] = visited[nx][j]
            else:
                visited[i][j] = visited[nx][j] + visited[i][ny]

print(visited[N-1][M-1])

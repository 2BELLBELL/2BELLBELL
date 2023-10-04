import sys
sys.setrecursionlimit(10**9)

# 전류를 흘린다
def dfs(x, y):
    # outer side 까지 도착한 경우 종료
    if x == M - 1:
        print('YES')
        exit()
    # 델타 탐색 진행
    for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        nx, ny = i+x, j+y
        # 벽을 넘지 않고, 미방문했으며, 전류가 흐를 수 있는 곳이면 재귀
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == 0:
            visited[nx][ny] = True
            dfs(nx, ny)

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
# outer side의 전류가 흐를 수 있고, 방문하지 않은 곳이면 전류를 흘려본다
for i in range(N):
    if arr[0][i] == 0 and visited[0][i] == False:
        visited[0][i] = True
        dfs(0, i)

# 안쪽까지 침투된 전류가 없으면 NO 출력
print('NO')
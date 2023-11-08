import sys
input = sys.stdin.readline


def dfs(r, c):
    global flag, cnt
    if flag:
        return
    if c == C - 1:
        flag = True
        cnt += 1
        return

    for i, j in [[-1, 1], [0, 1], [1, 1]]:
        nr, nc = i + r, j + c
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != 'x' and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc)
            if flag:
                break


R, C = map(int, input().split())
arr = [input() for _ in range(R)]
visited = [[False] * C for _ in range(R)]
cnt = 0
for r in range(R):
    flag = False
    dfs(r, 0)

print(cnt)
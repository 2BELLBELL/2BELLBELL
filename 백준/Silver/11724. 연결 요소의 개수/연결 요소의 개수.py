import sys
sys.setrecursionlimit(10**6)

def dfs(v):
    visited[v] = True
    for i in arr[v]:
        if visited[i] == False:
            dfs(i)

N, M = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)

# 재귀횟수 체크
cnt = 0
for i in range(1, N+1):
    if visited[i] == False:
        dfs(i)
        cnt += 1

print(cnt)
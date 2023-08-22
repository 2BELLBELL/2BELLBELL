import sys
input = sys.stdin.readline
def dfs(v):
    global cnt
    if visited.count(False) == 1:
        return

    visited[v] = True
    for i in arr[v]:
        if visited[i] == False:
            cnt += 1
            dfs(i)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 비행 노선 채우기
    arr = [[] for _ in range(N+1)]
    for _ in range(M):
        start, end = map(int, input().split())
        arr[start].append(end)
        arr[end].append(start)
    visited = [False] * (N+1)
    cnt = 0
    dfs(1)
    print(cnt)



def back(v, cnt):
    global answer
    if sum(visited) == 0 and cost[v][0] != 0:
        answer = min(answer, cnt + cost[v][0])
        return

    for i in arr[v]:
        if visited[i] == 1 and cnt + cost[v][i] < answer:
            visited[i] = 0
            back(i, cnt + cost[v][i])
            visited[i] = 1

N = int(input())
arr = [[] for _ in range(N)]
cost = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if cost[i][j] != 0:
            arr[i].append(j)
visited = [1] * N
visited[0] = 0
answer = 10**9
back(0, 0)
print(answer)
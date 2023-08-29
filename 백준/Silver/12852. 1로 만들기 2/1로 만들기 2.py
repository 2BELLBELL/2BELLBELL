from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = 0
    while True:
        tmp = q.popleft()
        if tmp == 1:
            return visited[tmp]
        if tmp % 3 == 0 and visited[tmp//3] == None:
            visited[tmp//3] = visited[tmp] + 1
            q.append(tmp//3)
        if tmp % 2 == 0 and visited[tmp//2] == None:
            visited[tmp // 2] = visited[tmp] + 1
            q.append(tmp // 2)
        if visited[tmp - 1] == None:
            visited[tmp - 1] = visited[tmp] + 1
            q.append(tmp - 1)

def dfs(v):
    stack.appendleft(v)
    if v == N:
        print(*stack)
        exit()
    if v*2 <= N and visited[v*2] != None and visited[v*2] == visited[v] - 1:
        dfs(v*2)
    if v*3 <= N and visited[v*3] != None and visited[v*3] == visited[v] - 1:
        dfs(v*3)
    if v+1 <= N and visited[v+1] != None and visited[v+1] == visited[v] - 1:
        dfs(v+1)


N = int(input())
visited = [None] * (N + 1)
cnt = 0
stack = deque()
print(bfs(N))
dfs(1)
import sys

# dfs 함수
def dfs(graph, v):
    stack = []
    visited = [False] * (N + 1)
    visited[v] = True
    print(v, end=' ')
    while True:
        for i in graph[v]:
            if not visited[i]:
                stack.append(v)
                v = i
                visited[v] = True
                print(v, end=' ')
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break

# bfs 함수
def bfs(graph, v):
    que = [v]
    visited = [False] * (N + 1)
    visited[v] = True
    print(v, end=' ')
    # 방문 순서 체크용
    while que:
        tmp = que.pop(0)
        for i in graph[tmp]:
            if visited[i] == False:
                que.append(i)
                visited[i] = True
                print(i, end=' ')


N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

# 간선 정보 입력 받기
for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

# 오름차순으로 방문하기 위한 정렬
for i in graph:
    i.sort()

# dfs 실행
dfs(graph, V)
# 줄바꿈
print()
# bfs 실행
bfs(graph, V)

import sys

def bfs(graph, v):
    global cnt
    que = [v]
    visited[v] = True
    answer[v] = cnt
    # 방문 순서 체크용
    while que:
        tmp = que.pop(0)
        for i in graph[tmp]:
            if visited[i] == False:
                que.append(i)
                visited[i] = True
                cnt += 1
                answer[i] = cnt


N, M, R = map(int, sys.stdin.readline().split())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
answer = [0] * (N+1)
cnt = 1
# 간선 정보 입력 받기
for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

# 오름차순으로 방문하기 위한 정렬
for i in graph:
    i.sort()

# bfs 실행
bfs(graph, R)

# 2번째 정점부터 도착순서 출력
for i in range(1, N+1):
    print(answer[i])
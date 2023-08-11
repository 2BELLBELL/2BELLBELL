# 정점의 개수
V = int(input())
# 간선의 개수
E = int(input())
# 각 노선 입력 받기
graph = [[0, 0]]
graph.extend([list(map(int, input().split())) for _ in range(E)])
# 바이러스 체크용 배열
visited = [False for _ in range(V + 1)]

def DFS(graph, visited, v):
    # 현재 정점은 감염처리
    visited[v] = True
    # 각 노선을 순회한다
    for i in graph:
        # 현재 노선에서 이어지는 노선이 있고, 그 노선을 미방문했다면
        if i[0] == v and visited[i[1]] == False:
            # 이어지는 노선으로 재귀한다
            DFS(graph, visited, i[1])
        # 역으로 이어지는 경우도 탐색
        elif i[1] == v and visited[i[0]] == False:
            DFS(graph, visited, i[0])

# 1번부터 바이러스 시작하는 함수 호출
DFS(graph, visited, 1)

# 1을 제외한 바이러스 걸린 컴퓨터의 개수 출력
print(visited.count(True) - 1)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(v, group):
    global result
    # 현재 좌표 방문 처리
    visited[v] = group
    # 현재 좌표와 연결된 정점을 순회한다
    for i in graph[v]:
        # 방문 하지 않은 인근 정점이 있으면 반대 그룹으로 방문처리되도록 dfs 재귀
        if visited[i] == 0:
            dfs(i, -group)
        # 방문 한 인근 정점 중, 같은 그룹이 있다면 이분 그래프가 아님
        elif visited[i] == group:
            result = 'NO'

# 테스트 케이스만큼 실행
K = int(input())
for tc in range(1, K + 1):
    V, E = map(int, input().split())
    # 간선 정보와 방문 여부 변수
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    # 이분 그래프를 판별할 변수
    result = 'YES'
    # 간선 정보 입력
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    # 각 정점마다 dfs 진행
    for i in range(1, V + 1):
        if visited[i] == 0:
            dfs(i, 1)
    # 모든 정점을 돌았을 때 이분그래프 여부 확인
    print(result)
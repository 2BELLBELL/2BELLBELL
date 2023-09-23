import sys
input = sys.stdin.readline
import heapq

def prim(graph, node):
    # 현재 노드 방문 처리
    visited[node] = True
    # 현재 노드를 최소힙으로 변경
    hq = graph[node]
    heapq.heapify(hq)
    weight = 0
    # 최소힙이 빌 때까지 (모든 노드를 방문 할 때까지)
    while hq:
        # 현재 노드에서 가중치가 가장 적은 간선을 선택
        w, n2 = heapq.heappop(hq)
        # 해당 간선이 미방문 상태라면 방문 후 가중치 더하기
        if not visited[n2]:
            visited[n2] = True
            weight += w
            # 해당 간선을 통한 노드에서 갈 수 있는 미방문 간선 정보를 힙에 삽입
            for i in graph[n2]:
                if not visited[i[1]]:
                    heapq.heappush(hq, i)
    return weight



V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
# 간선 정보를 가중치, 갈 수 있는 간선 순으로 정렬
for _ in range(E):
    n1, n2, w = map(int, input().split())
    graph[n1].append([w, n2])
    graph[n2].append([w, n1])

print(prim(graph, 1))
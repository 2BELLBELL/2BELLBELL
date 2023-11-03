import sys
input = sys.stdin.readline
import heapq

'''
v1 > v2를 거쳐서 N을 가는 최단 경로와
v2 > v1을 거쳐서 N을 가는 최단 경로 중 짧은 경로 계산
둘다 INF 상태면 -1 출력 
왜 틀렸지?
아 조건에서 오타
'''

def dijkstra(start, end):
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 꺼낸 간선의 길이가 현재 저장된 길이보다 길면 넘기기
        if dist > distance[now]:
            continue
        # 꺼낸 노드와 이어진 간선을 탐색
        for i in graph[now]:
            cost = i[1] + dist
            # 이어진 간선을 가는 방법 중, 꺼낸 노드를 통해 가는 방법이 더 빠른 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[end]


n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = int(1e9)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# 무조건 지나야하는 노선 경로
v1, v2 = map(int, input().split())
# 각 경로를 먼저 거쳐서 가는 최단 거리 계산
path_v1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
path_v2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)


if path_v1 >= INF and path_v2 >= INF:
    print(-1)
else:
    if path_v2 < path_v1:
        print(path_v2)
    else:
        print(path_v1)
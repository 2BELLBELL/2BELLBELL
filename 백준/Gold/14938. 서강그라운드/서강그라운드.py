import sys
input = sys.stdin.readline
import heapq

'''
각 노드별 dijkstra 알고리즘 돌려서 거리가 m 이하인 값의 합 중 최대값 구하기
'''

def dijkstra(start):
    q = []
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



n, m, r = map(int, input().split())
items_cnt = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
INF = int(1e9)
max_cnt = 0
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append([b, l])
    graph[b].append([a, l])

for i in range(1, n + 1):
    distance = [INF] * (n + 1)
    dijkstra(i)
    cnt = 0
    for j in range(1, n + 1):
        if distance[j] <= m:
            cnt += items_cnt[j - 1]
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
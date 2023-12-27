import sys
input = sys.stdin.readline
from collections import deque
import heapq
from itertools import combinations


def dijkstra(start):
    q = []
    distance = [int(1e9)] * (N + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append([b, 1])
        graph[b].append([a, 1])

arr = [[0]]
for i in range(1, N + 1):
    arr.append(dijkstra(i))

min_cnt = 10e9
min_idx = [1, 2]
for i, j in combinations(range(1, N + 1), 2):
    cnt = 0
    for x, y in zip(arr[i][1:], arr[j][1:]):
        cnt += min(x, y)
    if min_cnt > cnt * 2:
        min_cnt = cnt * 2
        min_idx = [i, j]

print(*min_idx, min_cnt)
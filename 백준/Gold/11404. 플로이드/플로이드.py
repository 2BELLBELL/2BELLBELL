import sys
input = sys.stdin.readline
import heapq


def dijkstra(start):
    q = []
    distance = [int(1e9)] * (n + 1)
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


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

for i in range(1, n + 1):
    for j in dijkstra(i)[1:]:
        if j != int(1e9):
            print(j, end=' ')
        else:
            print(0, end=' ')
    print()
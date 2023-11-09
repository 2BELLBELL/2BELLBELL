import sys
input = sys.stdin.readline

def bellmanFord(start):
    distance = [int(1e9)] * (N + 1)
    distance[start] = 0

    # N - 1번 탐색하며 마지막 차례엔 사이클 여부 확인
    for i in range(N):
        for j in range(M):
            s, e, dist = graph[j]
            if distance[s] == int(1e9):
                continue
            cost = dist + distance[s]
            if cost < distance[e]:
                distance[e] = cost
                if i == N - 1:
                    print(-1)
                    exit()
    return distance


N, M = map(int, input().split())
graph = []
for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append([A, B, C])

distance = bellmanFord(1)

for i in range(2, N + 1):
    if distance[i] != int(1e9):
        print(distance[i])
    else:
        print(-1)
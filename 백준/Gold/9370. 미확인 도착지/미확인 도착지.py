import sys
input = sys.stdin.readline
from collections import deque
import heapq


'''
s에서 목적지까지 가는 최단 경로가 g > h or h > g 를 거쳐서 가는 최단 경로와 같다면
그들의 목적지 중 하나이다.
다익스트라를 매 도착지마다 실행한다면 시간초과,,,!
타입에러 이유는..?
int(1e9) != 100000000 뭔 차이지
'''

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

T = int(input())
for _ in range(T):
    # 교차로, 도로, 목적지 후보의 개수
    n, m, t = map(int, input().split())
    # 출발지, 지나간 도로 정보 (g > h)
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        # a 와 b 사이에 가중치 d
        a, b, d = map(int, input().split())
        graph[a].append([b, d])
        graph[b].append([a, d])
    # 목적지 후보
    ends = [int(input()) for _ in range(t)]
    # 미리 목적지 별 다익스트라 해놓기
    dist_s = dijkstra(s)
    dist_g = dijkstra(g)
    dist_h = dijkstra(h)
    answer = []
    for i in ends:
        if dist_s[g] + dist_g[h] + dist_h[i] == dist_s[i] or dist_s[h] + dist_h[g] + dist_g[i] == dist_s[i]:
            answer.append(i)

    print(*sorted(answer))

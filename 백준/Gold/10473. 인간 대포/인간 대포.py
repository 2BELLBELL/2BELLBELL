import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq
import math


def dijkstra(start):
    q = []
    INF = int(1e9)
    times = [INF] * (n + 2)
    heapq.heappush(q, (0, start))
    times[start] = 0

    while q:
        time, now = heapq.heappop(q)
        # 꺼낸 시간이 현재 저장된 시간보다 길면 넘기기
        if time > times[now]:
            continue
        # 꺼낸 노드와 이어진 간선을 탐색
        for i in graph[now]:
            # print(i)
            tmp_time = i[1]
            go_time = time + tmp_time
            # print(go_time, times[i[0]])

            # 이어진 간선을 가는 방법 중, 꺼낸 노드를 통해 가는 방법이 더 빠른 경우
            if go_time < times[i[0]]:
                times[i[0]] = go_time
                heapq.heappush(q, (go_time, i[0]))

    return times


start = list(map(float, input().split()))
end = list(map(float, input().split()))
n = int(input())
cannons = [start] + [list(map(float, input().split())) for _ in range(n)] + [end]
graph = [[] for _ in range(n + 2)]
for i in range(n + 2):
    for j in range(n + 2):
        if i == j:
            continue
        # 좌표 사이의 거리
        tmp_dist = math.sqrt((cannons[i][0] - cannons[j][0])**2 + (cannons[i][1] - cannons[j][1])**2)
        # 걸어가는 속도
        walk_time = tmp_dist / 5
        # 대포타고 날아가는 속도
        cannon_time = 2 + abs((tmp_dist - 50) / 5)
        # 시작점인경우 무조건 대포까지 걸어가야함
        if i == 0:
            time = walk_time
        else:
            time = min(walk_time, cannon_time)
        # 노드번호, 도착시간을 그래프에 삽입
        graph[i].append((j, time))
print(dijkstra(0)[n+1])
import sys
input = sys.stdin.readline
# from collections import deque
# sys.stdin = open('input.txt')
import heapq
# from itertools import combinations
sys.setrecursionlimit(10**9)
import math

def prim():
    # 현재 노드를 최소힙으로 변경
    hq = []
    heapq.heappush(hq, (0, 0))
    # 정답 거리
    answer = 0

    # 최소힙이 빌 때까지 (모든 노드를 방문 할 때까지)
    while hq:
        # 현재 노드에서 가중치가 가장 적은 간선을 선택
        dist, star = heapq.heappop(hq)
        # 해당 간선이 미방문 상태라면 방문 후 가중치 더하기
        if not visited[star]:
            visited[star] = True
            answer += dist
            # 해당 간선을 통한 노드에서 갈 수 있는 간선 정보를 힙에 삽입
            for i in range(n):
                new_star = graph[star][i]
                heapq.heappush(hq, (new_star, i))
    return answer


n = int(input())
arr = [list(map(float, input().split())) for _ in range(n)]
graph = [[0] * n for _ in range(n)]
visited = [False] * n

# 직접 가중치 계산.. 피타고라스
for i in range(n):
    for j in range(n):
        graph[i][j] = math.sqrt((arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2)

# print(graph)
print(prim())


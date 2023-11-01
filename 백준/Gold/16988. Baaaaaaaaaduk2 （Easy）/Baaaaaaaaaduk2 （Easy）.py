import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline
# import numpy as np
from itertools import combinations
from collections import deque


'''
보드를 돌며 2인 곳을 발견하면 visited, cnt, rock 생성 후 bfs 진행
델타 탐색하며 
1. False 인 0을 발견하면 cnt 를 증가시키고 visited2 에 true 처리
2. False 인 2를 발견하면 rock 을 증가시키고 visited1 에 true 처리
탐색이 끝나을 때 cnt 가 2 이하면 max 값을 rock 으로 갱신
'''


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    visited_0 = [[False] * M for _ in range(N)]
    cnt = 0
    rock = 1
    rock_tmp_list = []
    while q:
        tmp_x, tmp_y = q.popleft()
        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = i + tmp_x, j + tmp_y
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 2 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    rock += 1
                    q.append((nx, ny))
                elif board[nx][ny] == 0 and not visited_0[nx][ny]:
                    visited_0[nx][ny] = True
                    rock_tmp_list.append([nx, ny])
                    cnt += 1

    if cnt <= 2:
        global rock_list1, rock_list2
        rock_list2.extend(rock_tmp_list)
        rock_tmp_list.append(rock)
        rock_list1.append(rock_tmp_list)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
rock_list1 = []
rock_list2 = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 2 and not visited[i][j]:
            bfs(i, j)

tmp_list = []
for i in rock_list2:
    if i not in tmp_list:
        tmp_list.append(i)

# print(rock_list1)
# print(rock_list2)
# print(tmp_list)

if not rock_list1:
    print(0)
elif len(tmp_list) == 1:
    max_cnt = 0
    for i in rock_list1:
        if len(i) == 2 and tmp_list[0] in i:
            max_cnt += i[1]
    print(max_cnt)
else:
    max_cnt = 0
    for i in combinations(tmp_list, 2):
        cnt = 0
        for j in rock_list1:
            if len(j) == 3 and i[0] in j and i[1] in j:
                cnt += j[2]
            elif len(j) == 2 and j[0] in i:
                cnt += j[1]
        max_cnt = max(max_cnt, cnt)
    print(max_cnt)
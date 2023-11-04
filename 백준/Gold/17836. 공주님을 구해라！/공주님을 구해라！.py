'''
왜 틀렸는지 모르겠는 코드.. 80%에서 실패

import sys
input = sys.stdin.readline
from collections import deque


def bfs():
    q = deque()
    q.append((0, 0, False, 0))
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    gram_cnt = 999999999

    while q:
        x, y, gram, time = q.popleft()
        if x == N - 1 and y == M - 1:
            if gram_cnt > time:
                print(time)
                exit()
            else:
                print(gram_cnt)
                exit()
        if T < time:
            if gram_cnt != 999999999:
                print(gram_cnt)
            else:
                print("Fail")
                exit()
        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = x+i, y+j
            # 그람이 없는 경우
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and not gram:
                # 갈 수 있는 공간을 발견
                if arr[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny, False, time + 1))
                # 그람을 발견
                if arr[nx][ny] == 2:
                    if (N - 1 - nx) + (M - 1 - ny) > T:
                        print("Fail")
                        exit()
                    else:
                        visited[nx][ny] = True
                        gram_cnt = (time + 1 + (N - 1 - nx) + (M - 1 - ny))


    if gram_cnt != 999999999 and gram_cnt <= T:
        print(gram_cnt)
    else:
        print("Fail")

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
bfs()
'''

import sys
from collections import deque
input = sys.stdin.readline
N, M, T = map(int,input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
m = [list(map(int,input().split())) for _ in range(N)]
q = deque()
visited = [[0] * M for _ in range(N)]
 
def bfs():
    gram = 10001
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        # 공주님이 있는 곳에 도착했을 때
        if (x, y) == (N-1, M-1):
            return min(visited[x][y]-1, gram)
        # 그람이 있는 곳에 도착했을 때
        if m[x][y] == 2:
            gram = visited[x][y]-1 + N-1-x + M-1-y
 
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if m[nx][ny] == 0 or m[nx][ny] == 2:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return gram
 
res = bfs()
if res > T:
    print('Fail')
else:
    print(res)
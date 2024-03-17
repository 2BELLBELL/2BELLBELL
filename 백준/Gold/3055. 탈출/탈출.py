import sys
input = sys.stdin.readline
from collections import deque


def move_water():
    q = deque()
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '*':
                arr[i][j] = str(0)
                q.append((i, j, 0))

    while q:
        x, y, cnt = q.popleft()
        for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + i, y + j
            if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] == '.':
                q.append((nx, ny, cnt + 1))
                arr[nx][ny] = str(cnt)


def move_dochi():
    q = deque()
    visited = [[False] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'S':
                q.append((i, j, 0))
                visited[i][j] = 'S'
                start = (i, j)
            elif arr[i][j] == 'D':
                end = (i, j)
                visited[i][j] = 'D'
    while q:
        x, y, cnt = q.popleft()
        for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + i, y + j
            if 0 <= nx < R and 0 <= ny < C:
                if arr[nx][ny] == 'D':
                    print(cnt + 1)
                    exit()
                if arr[nx][ny].isdigit() and int(arr[nx][ny]) > cnt and not visited[nx][ny]:
                    q.append((nx, ny, cnt + 1))
                    visited[nx][ny] = cnt
                elif arr[nx][ny] == '.' and not visited[nx][ny]:
                    q.append((nx, ny, cnt + 1))
                    visited[nx][ny] = cnt
    print('KAKTUS')

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
move_water()
move_dochi()
import sys
input = sys.stdin.readline
from collections import deque


def bfs():
	q = deque()
	q.append((Hx - 1, Hy - 1, 1, 0))
	visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
	visited[Hx - 1][Hy - 1][1] = True

	while q:
		tmp_x, tmp_y, magic, cnt = q.popleft()
		if (tmp_x, tmp_y) == (Ex - 1, Ey - 1):
			print(cnt)
			exit()
		for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
			nx, ny = tmp_x + i, tmp_y + j
			if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][magic]:
				if arr[nx][ny] == 1 and magic:
					visited[nx][ny][0] = True
					q.append((nx, ny, 0, cnt + 1))
				elif arr[nx][ny] == 0:
					visited[nx][ny][magic] = True
					q.append((nx, ny, magic, cnt + 1))
	print(-1)


N, M = map(int, input().split())
Hx, Hy = map(int, input().split())
Ex, Ey = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
bfs()
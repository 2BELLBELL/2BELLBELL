import sys
input = sys.stdin.readline
from collections import deque


'''
돌 100,000개 중 동규는 N번, 주미는 M번에 위치
[1, -1, A, -A, B, -B, N*A, N*B]
'''


def bfs():
	arr = [False] * 100001
	q = deque()
	q.append((N, 0))

	while q:
		location, cnt = q.popleft()
		if location == M:
			print(cnt)
			break
		for i in [location + 1, location - 1, location + A, location - A, location + B, location - B, location * A, location * B]:
			if 0 <= i <= 100000 and not arr[i]:
				arr[i] = True
				q.append((i, cnt + 1))


A, B, N, M = map(int, input().split())
bfs()
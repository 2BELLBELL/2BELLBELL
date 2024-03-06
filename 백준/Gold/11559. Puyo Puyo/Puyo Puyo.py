import sys
input = sys.stdin.readline
from collections import deque


'''
1. 뿌요 터트리기 (터트릴 뿌요가 없으면 종료)
2. 뿌요 하강
'''


# 뿌요 터트리기
def puyo_remove(x, y):
	q = deque()
	puyo_list = set()
	puyo_list.add((x, y))
	q.append((x, y))

	while q:
		tmp_x, tmp_y = q.popleft()
		for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
			nx, ny = tmp_x + i, tmp_y + j
			if 0 <= nx < 12 and 0 <= ny < 6 and arr[nx][ny] == arr[x][y] and (nx, ny) not in puyo_list:
				q.append((nx, ny))
				puyo_list.add((nx, ny))
				visited[nx][ny] = True

	if len(puyo_list) >= 4:
		global flag
		flag = False
		for i, j in puyo_list:
			arr[i][j] = '.'


# 뿌요 내리기
def puyo_down():
	for i in range(6):
		tmp = []
		for j in range(12):
			if arr[j][i] != '.':
				tmp.append(arr[j][i])
		if tmp:
			tmp = ['.'] * (12 - len(tmp)) + tmp
			for k in range(12):
				arr[k][i] = tmp[k]


arr = [list(input()) for _ in range(12)]
answer = 0

while True:
	flag = True
	visited = [[False] * 6 for _ in range(12)]
	for i in range(12):
		for j in range(6):
			if arr[i][j] != '.' and not visited[i][j]:
				puyo_remove(i, j)
	# 터진 뿌요가 없으면 중지
	if flag:
		break
	# 터진 뿌요가 있으면 연쇄+1, 뿌요 내리기
	else:
		answer += 1
		puyo_down()

print(answer)
import sys
input = sys.stdin.readline
from itertools import permutations
import copy


def rotation(graph):
	for j in range(s):
		tmp = graph[r - s + j][c - s + j]
		for i in range(r - s + j, r + s - j):
			graph[i][c - s + j] = graph[i + 1][c - s + j]
		for i in range(c - s + j, c + s-j):
			graph[r + s - j][i] = graph[r + s - j][i+1]
		for i in range(r + s - j, r - s + j, -1):
			graph[i][c + s - j] = graph[i - 1][c + s - j]
		for i in range(c + s - j, c - s + j, -1):
			graph[r - s + j][i] = graph[r - s + j][i - 1]

		graph[r - s + j][c - s + 1 + j] = tmp


N, M, K = map(int, input().split())
arr = [0] + [[0] + list(map(int, input().split())) for _ in range(N)]
rotate = [list(map(int, input().split())) for _ in range(K)]
answer = 10**9

for i in permutations(rotate):
	tmp_arr = copy.deepcopy(arr)

	for r, c, s in i:
		rotation(tmp_arr)

	for i in range(1, N + 1):
		answer = min(answer, sum(tmp_arr[i]))

print(answer)
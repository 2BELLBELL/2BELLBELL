import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append(['.'] * 9 + [0])
    while q:
        tmp_board = q.popleft()
        if tmp_board[:9] == board:
            print(tmp_board[9])
            return

        for i in [[0, 1, 3], [0, 1, 2, 4], [1, 2, 5], [0, 3, 4, 6], [1, 3, 4, 5, 7],
                  [2, 4, 5, 8], [3, 6, 7], [4, 6, 7, 8], [5, 7, 8]]:
            tmp_board2 = tmp_board[:]
            for j in i:
                if tmp_board2[j] == '*':
                    tmp_board2[j] = '.'
                else:
                    tmp_board2[j] = '*'
            tmp_board2[9] += 1
            if tuple(tmp_board2[:9]) not in visited:
                q.append(tmp_board2)
                visited.add(tuple(tmp_board2[:9]))


T = int(input().strip())
for _ in range(T):
    board = []
    visited = set()
    for _ in range(3):
        board.extend(input().strip())
    bfs()
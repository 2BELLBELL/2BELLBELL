import sys
input = sys.stdin.readline


'''
환형 = 벽을 넘으면 반대편으로 텔포 가능
'''


def dfs(x, y, word):
    for i, j in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
        nx, ny = (x + i) % N, (y + j) % M
        if nx == -1:
            nx = N - 1
        if ny == -1:
            ny = M - 1
        if len(word) < god_words_max_length:
            if word + arr[nx][ny] in word_dict.keys():
                word_dict[word + arr[nx][ny]] += 1
            else:
                word_dict[word + arr[nx][ny]] = 1
            dfs(nx, ny, word + arr[nx][ny])


N, M, K = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
word_dict = {}
god_words = [input().strip() for _ in range(K)]
god_words_max_length = 0
for i in god_words:
    god_words_max_length = max(god_words_max_length, len(i))

       
for i in range(N):
    for j in range(M):
        if arr[i][j] in word_dict:
            word_dict[arr[i][j]] += 1
        else:
            word_dict[arr[i][j]] = 1
        dfs(i, j, arr[i][j])

for i in god_words:
    if i in word_dict.keys():
        print(word_dict[i])
    else:
        print(0)
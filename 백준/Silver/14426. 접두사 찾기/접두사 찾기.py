import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = 0

# 전체 접두 가능성 단어 저장
arr = set()

for _ in range(N):
    word = input().strip()
    for i in range(1, len(word) + 1):
        arr.add(word[:i])

for _ in range(M):
    word = input().strip()
    if word in arr:
        cnt += 1

print(cnt)
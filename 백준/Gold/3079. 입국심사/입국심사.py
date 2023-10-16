import sys
input = sys.stdin.readline

'''
N개의 심사대와, M명의 상근이 친구
최솟값
'''
N, M = map(int, input().split())
table = []
for _ in range(N):
    table.append(int(input()))
table.sort()

start = min(table)
end = max(table) * M
while start < end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(N):
        cnt += mid // table[i]
        if table[i] > mid:
            break
    if cnt >= M:
        end = mid
    elif cnt < M:
        start = mid + 1

print(start)
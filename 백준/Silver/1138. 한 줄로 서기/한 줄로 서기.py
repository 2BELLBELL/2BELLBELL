N = int(input())
arr = list(map(int, input().split()))
num = list(range(1, N + 1))
line = [0] * N

for i in range(N):
    cnt = arr[i]
    for j in range(N):
        if cnt == 0 and line[j] == 0:
            line[j] = i + 1
            break
        if line[j] == 0:
            cnt -= 1

print(*line)
N = int(input())
answer = 0
trip = set()

for i in range(1, N):
    for j in range(i, N):
        k = N - i - j
        if j <= k and i + j > k:
            answer += 1

print(answer)
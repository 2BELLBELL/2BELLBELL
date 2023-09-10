N = int(input())
M = int(input())
arr = list(range(N + 1))
light = list(map(int, input().split()))
answer = 0
for i in range(M):
    if i == 0:
        tmp = light[i]
    elif i == (M - 1):
        tmp = N - light[i]
    else:
        tmp = ((light[i] + light[i + 1] + 1) // 2) - light[i]
    answer = max(answer, tmp)

if M == 1:
    answer = max(light[0], N - light[0])

print(answer)
N, K = map(int, input().split())
arr = []
rank = 1
for _ in range(N):
    num, g, s, c = map(int, input().split())

    if g == 0:
        g = 1000001
    if s == 0:
        s = 1000001
    if c == 0:
        c = 1000001

    arr.append([g, s, c, num])

arr.sort()

for i in range(N - 1):
    if arr[i][3] == K:
        print(rank)
        break
    if arr[i][0] == arr[i+1][0] and arr[i][1] == arr[i+1][1] and arr[i][2] == arr[i+1][2]:
        pass
    else:
        rank += 1



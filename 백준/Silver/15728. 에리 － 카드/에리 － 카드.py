N, K = map(int, input().split())
share_card = list(sorted(map(int, input().split())))
team_card = list(sorted(map(int, input().split())))

result = []
for i in team_card:
    for j in share_card:
        result.append([i * j, i])
result.sort()

numbers = set()
for i in range(len(sorted(result)), 0, -1):
    if result[i - 1][1] not in numbers:
        numbers.add(result[i - 1][1])
        K -= 1
    if K < 0:
        print(result[i - 1][0])
        break
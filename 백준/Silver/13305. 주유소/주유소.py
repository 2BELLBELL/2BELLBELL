N = int(input())
dis = list(map(int, input().split()))
oil = list(map(int, input().split()))

# 처음은 무조건 이동
answer = dis[0] * oil[0]
# 현재까지 가장 싼 주유소의 위치
idx = 0
for i in range(1, N - 1):
    # 현재 도시의 기름 값이 더 싸면 교체
    if oil[idx] > oil[i]:
        idx = i
    # 다음 도시까지 갈 수 있는 기름양 주유
    answer += dis[i] * oil[idx]

print(answer)
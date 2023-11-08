import sys
input = sys.stdin.readline

# 물웅덩이의 수, 널빤지의 길이
N, L = map(int, input().split())
pools = []
for _ in range(N):
    s, e = map(int, input().split())
    pools.append([s, e])

pools.sort(key=lambda x:x[0])

cnt = 0
# 널빤지의 끝 위치
max_v = 0
for i in range(N):
    if max_v >= pools[i][0]:
        pools[i][0] = max_v + 1
    # print(pools[i], cnt)
    # 물 웅덩이만 보고 더하기
    cnt2 = (pools[i][1] - pools[i][0]) // L
    cnt += (pools[i][1] - pools[i][0]) // L
    # 나머지가 있으면 1 추가로 더해주기
    if (pools[i][1] - pools[i][0]) % L != 0:
        cnt += 1
        cnt2 += 1

    max_v = pools[i][0] - 1 + cnt2 * L

print(cnt)
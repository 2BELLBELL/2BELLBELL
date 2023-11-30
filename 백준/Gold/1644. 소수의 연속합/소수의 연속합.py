N = int(input())
primes = []
# 에라토스테네스의 체 구현
a = [False, False] + [True] * (N-1)
for i in range(2, N + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, N + 1, i):
            a[j] = False
# print(primes)

s, e, cnt = 0, 0, 0
while e <= len(primes):
    # 현재 소수들의 합이 N과 같다면 정답 카운트 후, 엔드 포인터 이동
    if sum(primes[s:e]) == N:
        cnt += 1
        e += 1
    # 현재 소수들의 합이 N보다 작다면, 엔드 포인터만 이동
    elif sum(primes[s:e]) < N:
        e += 1
    # 현재 소수들의 합이 N보다 크다면, 스타트 포인터만 이동
    else:
        s += 1

print(cnt)
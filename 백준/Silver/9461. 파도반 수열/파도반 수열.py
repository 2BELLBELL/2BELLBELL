import sys
T = int(input())

memo = [0] * 101
memo[1] = memo[2] = memo[3] = 1


def P(n):
    # 메모이제이션에 차있으면 바로 꺼내기
    if memo[n] != 0:
        return memo[n]
    # 메모이제이션 활용
    memo[n] = P(n - 2) + P(n - 3)

    return memo[n]

for tc in range(1, T + 1):
    n = int(input())
    print(P(n))

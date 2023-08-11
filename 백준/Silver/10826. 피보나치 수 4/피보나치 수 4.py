import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

n = int(input())
memo = [0] * 10001
memo[0] = 0
memo[1] = memo[2] = 1


def pibo(n):
    global memo
    # 메모이제이션에 차있으면 바로 꺼내기
    if n == 0:
        return 0
    if memo[n] != 0:
        return memo[n]
    # 메모이제이션 활용
    memo[n] = pibo(n - 1) + pibo(n - 2)

    return memo[n]

print(pibo(n))
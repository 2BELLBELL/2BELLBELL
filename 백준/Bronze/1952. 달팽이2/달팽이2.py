import sys
M, N = map(int, sys.stdin.readline().split())

# 행이 더 큰 경우
if M > N:
    print((N * 2) - 1)
# 행과 열이 같거나 열이 더 큰 경우
else:
    print((M - 1) * 2)
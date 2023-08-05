import sys

# N과 K의 수를 입력 받는다
N, K = map(int, sys.stdin.readline().split())

divisor = []

# N의 약수를 리스트에 순서대로 삽입한다
for i in range(1, N + 1):
    if N % i == 0:
        divisor.append(i)

# 전체 약수의 수가 K보다 크면 K번째 약수를 출력
if len(divisor) >= K:
    print(divisor[K - 1])
# 전체 약수의 수가 K보다 작으면 0을 출력
else:
    print(0)
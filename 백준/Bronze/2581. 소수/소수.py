import sys

# N과 M의 수를 입력 받는다
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

# 소수 변수
prime_numbers = []

# N과 M사이의 소수를 변수에 삽입한다
for i in range(M, N + 1):
    check = 0
    for j in range(1, i):
        if i % j == 0:
            check += 1
    if check == 1:
        prime_numbers.append(i)

# 소수의 목록이 1개 이상이면 합과 최솟값 출력
if len(prime_numbers) >= 1:
    print(sum(prime_numbers))
    print(min(prime_numbers))
# 소수 목록이 비어있으면 -1 출력
else:
    print(-1)
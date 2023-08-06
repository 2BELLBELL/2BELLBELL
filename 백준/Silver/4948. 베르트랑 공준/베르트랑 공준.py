import sys

# 소수인지 확인
def decimal(x):
    if x == 1:
        return False
    for k in range(2, int(x**0.5)+1):
        if x % k == 0:
            return False
    return True

# 가능한 모든 수가 소수인지 확인
decimal_nums = []
for i in range(2, 246912):
    if decimal(i):
        decimal_nums.append(i)

# 반복문을 통해 케이스를 확인
while True:
    n = int(sys.stdin.readline())
    cnt = 0

    # 입력받은 수가 0이면 반복을 멈춤
    if n == 0:
        break

    # 소수인 수를 반복하여 구간에 있는지 확인
    for j in decimal_nums:
        # 구간에 있다면 카운트
        if n < j <= 2 * n:
            cnt += 1
    print(cnt)
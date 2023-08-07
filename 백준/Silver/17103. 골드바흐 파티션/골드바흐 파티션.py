import sys

T = int(sys.stdin.readline())

# 에라토스테네스의 체를 활용하여 미리 소수 판별해두기
arr = [0] * 1000001
prime = []
# 0과 1은 미리 판별
arr[0], arr[1] = 1, 1
for i in range(2, 1000001):
    if arr[i] == 0:
        prime.append(i)
        for j in range(i*2, 1000001, i):
            arr[j] = 1

# 테스트 케이스의 수만큼 반복 시행
for tc in range(1, T + 1):
    N = int(sys.stdin.readline())
    cnt = 0
    for i in prime:
        if i >= N:
            break
        if not arr[N - i] and i <= N - i:  # 순서만 다른거 counting 하지 않기 위해
            cnt += 1
    print(cnt)
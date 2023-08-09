import sys

# 자연수 입력 받기
M, N = map(int, sys.stdin.readline().split())

for i in range(M, N + 1):
    # 1은 예외처리
    if i == 1:
        continue
    cnt = 0
    # i의 제곱근 +1 까지 선회하며 나누어지는 여부 확인
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            cnt += 1
            break
    # 0으로 나누어떨어진 값이 없다면 해당 숫자는 소수
    if cnt == 0:
        print(i)




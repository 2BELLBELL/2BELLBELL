import sys
N = int(sys.stdin.readline())

# 소수 찾기 함수 
def check(x):
    # 2부터 해당 수의 제곱근 + 1까지 탐색
    for i in range(2, int(x**0.5) + 1):
        # 0으로 나누어지는게 있으면 False 반환
        if x % i == 0:
            return False
    # 아니면 True 반환
    return True

for i in range(N):
    n = int(sys.stdin.readline())
    while True:
        # 0이나 1은 무조건 2반환
        if n == 0 or n == 1:
            print(2)
            break
        if check(n):
            print(n)
            break
        else:
            n += 1
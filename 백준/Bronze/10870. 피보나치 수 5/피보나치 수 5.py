# 피보나치 수 재귀함수 생성
def pibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return pibo(n - 1) + pibo(n - 2)

n = int(input())

print(pibo(n))
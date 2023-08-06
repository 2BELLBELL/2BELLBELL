# 입력 값 받기
A, B = map(int, input().split())
C, D = map(int, input().split())

# 분수 덧셈
x, y = A*D + C*B, B*D

# 최대 공약수 구하기
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최대 공약수로 약분하기
print(x // gcd(y, x), y // gcd(y, x))
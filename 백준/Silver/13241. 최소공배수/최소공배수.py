# 입력 값 받기
a, b = map(int, input().split())

# 최대 공약수 구하기
def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

# 최소 공배수 구하기
print(a * b // gcd(a, b))
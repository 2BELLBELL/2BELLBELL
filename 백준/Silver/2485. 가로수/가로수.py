import sys
# 입력 값 받기
N = int(sys.stdin.readline())

arr = [int(sys.stdin.readline()) for _ in range(N)]

# 각 간격의 차를 저장할 변수
minus = []
for i in range(len(arr) - 1):
    minus.append(arr[i + 1] - arr[i])

# 최대 공약수 함수 생성
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 각 간격의 차의 최대 공약수 구하기
result = minus[0]
for i in range(len(minus) - 1):
    if result > minus[i]:
        result = gcd(result, minus[i])
    elif result < minus[i]:
        result = gcd(minus[i], result)

# 간격의 차를 돌며 최대 공약수로 나누고 -1 해준 값을 더한다
total = 0
for i in minus:
    total += i // result - 1

print(total)

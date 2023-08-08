N = int(input())

# 다이나믹 프로그래밍 연습용 12까지 팩토리얼 다 구해놓기
arr = [0] * 13
# 0! 1! 은 1로 설정
arr[0], arr[1] = 1, 1

# 메모이제이션용 함수
def fac(n):
    if arr[n] != 0:
        return arr[n]

    arr[n] = n * fac(n - 1)
    return arr[n]

# 12까지 arr[n]에 저장
fac(12)

print(arr[N])
import sys
X, Y = map(int, sys.stdin.readline().split())

# 숫자뒤집기 함수 정의
def Rev(n):
    # 숫자를 문자열로 변경 후 리스트화
    n = list(str(n))
    # 내장함수 금지지만 len은 어차피 구현 가능해서 시간 단축용으로 썼습니다..
    cnt = len(n) - 1
    new_n = 0
    # 문자를 역순으로 탐색
    for i in n[::-1]:
        # 0을 만나면 cnt 를 -1
        if i == '0':
            cnt -= 1
        # 0이 아니면 i에 10의 cnt제곱만큼 곱한 값을 더한다
        if i != '0':
            new_n += int(i) * 10**cnt
            cnt -= 1
    return new_n

print(Rev(Rev(X) + Rev(Y)))
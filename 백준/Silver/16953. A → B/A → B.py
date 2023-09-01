# 2가지 경우의 수에 대해 dfs 실행
def dfs(x, y):
    cnt = 1
    while True:
        # 현재 숫자와 만들고자하는 숫자가 같으면 연산 횟수 반환
        if x == y:
            return cnt
        # 현재 숫자가 목표 숫자를 지나쳐서 더 작아졌으면 -1 반환
        elif x < y:
            return -1

        # 현재 숫자가 2로 나눠진다면 나누기
        if x % 2 == 0:
            x //= 2
            cnt += 1
        # 현재 숫자의 마지막 숫자가 1이라면 10으로 나누기
        elif list(map(int, str(x)))[-1] == 1:
            x //= 10
            cnt += 1
        # 목표 숫자에 도달하기 전에 해당 조건이 없으면 -1 반환
        else:
            return -1
A, B = map(int, input().split())
print(dfs(B, A))
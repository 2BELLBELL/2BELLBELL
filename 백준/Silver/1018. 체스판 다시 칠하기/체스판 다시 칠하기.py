import sys

# N과 K의 수를 입력 받는다
N, M = map(int, sys.stdin.readline().split())

# 완벽하게 칠해진 리스트 생성
perpect_list = []
for _ in range(4):
    perpect_list.append(list('WBWBWBWB'))
    perpect_list.append(list('BWBWBWBW'))

# 예제 리스트 생성
N_list = []
for i in range(N):
    N_list.append(list(sys.stdin.readline().strip()))

# 칠해야하는 개수 모음 리스트
result = []

# Y축 이동용
Y1 = 0
Y2 = 8
# Y축 이동 횟수
for Y in range(N - 7):
    # X축 이동용
    X1 = 0
    X2 = 8
    # X축 이동 횟수
    for X in range(M - 7):
        # 완벽 리스트와 예제 리스트 비교
        cnt = 0
        for P_list, N_list2 in zip(perpect_list, N_list[Y1:Y2]):
            for x, y in zip(range(0, 8), range(X1, X2)):
                if P_list[x] == N_list2[y]:
                    cnt += 1

        # 최소 횟수 보정
        if cnt > 32:
            cnt = 64 - cnt

        # 리설트 값에 더하기
        result.append(cnt)

        # X축 이동
        X1 += 1
        X2 += 1

    # Y축 이동
    Y1 += 1
    Y2 += 1

print(min(result))

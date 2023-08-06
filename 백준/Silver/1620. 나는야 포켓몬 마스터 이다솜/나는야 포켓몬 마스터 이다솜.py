import sys
N, M = map(int, sys.stdin.readline().split())

# 포켓몬 도감 딕셔너리 생성
# 숫자 - 포켓몬 형식
num_poketmon = {}
# 포켓몬 - 숫자 형식
poketmon_num = {}

# 포켓몬 도감 채워넣기
for i in range(N):
    poketmon = sys.stdin.readline().rstrip()
    num_poketmon[i] = poketmon
    poketmon_num[poketmon] = i

# M 개를 순차 검사
for _ in range(M):
    answer = sys.stdin.readline().rstrip()
    # 정수로 변환이 가능한 경우 숫자 - 포켓몬에서 찾기
    if answer.isdigit():
        print(num_poketmon[int(answer) - 1])
    # 안되면 포켓몬 - 숫자 형식에서 찾기
    else:
        print(poketmon_num[answer] + 1)

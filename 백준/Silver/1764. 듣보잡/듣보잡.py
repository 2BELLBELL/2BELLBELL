import sys
N, M = map(int, sys.stdin.readline().split())

# 듣도 못한 사람과 보도 못한 사람 변수
listen = set()
see = set()

# 듣도 못한 사람 채우기
for i in range(N):
    listen.add(sys.stdin.readline().rstrip())

# 보도 못한 사람 채우기
for _ in range(M):
    see.add(sys.stdin.readline().rstrip())

# 듣도 보도 못한 사람 찾기
result = see.intersection(listen)

# 듣보잡 수 출력
print(len(result))

# 듣보잡 사전순으로 리스트화
result = sorted(result)

# 듣보잡 명단 출력
for people in result:
    print(people)
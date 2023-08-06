import sys
N, M = map(int, sys.stdin.readline().split())

# 집합 S 와 포함 여부 카운팅 변수 생성
S = set()
cnt = 0

# N 만큼 집합 S 에 추가한다
for _ in range(N):
    S.add(sys.stdin.readline())

# M 개의 줄을 검사하며 S 에 있는지 카운팅
for _ in range(M):
    if sys.stdin.readline() in S:
        cnt += 1
        
# cnt 출력
print(cnt)
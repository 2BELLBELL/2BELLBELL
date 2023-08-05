import sys

# 좌표의 개수
T = int(sys.stdin.readline())

result = []

# 숫자 넣기
for i in range(1, T + 1):
    result.append(int(sys.stdin.readline()))

# 정렬한 숫자를 순서대로 출력
for i in sorted(result):
    print(i)

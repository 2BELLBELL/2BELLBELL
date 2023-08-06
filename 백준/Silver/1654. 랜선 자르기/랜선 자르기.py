import sys

# 입력 값 받기
K, N = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline().strip()) for _ in range(K)]

start = 1
end = max(arr)
possible = []

while start <= end:
    # 중간 값 갱신
    mid = (start + end) // 2

    # 가져갈 수 있는 랜선의 수
    line = 0

    # 가지고 있는 랜선을 선회하며
    for i in arr:
        line += i // mid

    # 만들 수 있는 랜선 개수가 필요한 랜선 개수보다 같거나 크면
    # 가능성 리스트에 저장 후 더 높은 범위에서 탐색
    if line >= N:
        possible.append(mid)
        start = mid + 1

    # 만들 수 있는 랜선 개수가 더 적다면
    elif line < N:
        end = mid - 1

# 랜선 리스트에서 최댓값 출력
if len(possible) != 0:
    print(max(possible))
else:
    print(K)
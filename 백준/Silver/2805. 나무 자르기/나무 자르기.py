import sys

# 입력 값 받기
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

bottom = 0
top = max(arr)
possible = []

while bottom <= top:
    # 중간 값 갱신
    mid = (bottom + top) // 2

    # 상근이가 들고 갈 나무
    wood = 0

    # 나무 리스트를 선회하며
    for i in arr:
        # 절단기보다 나무가 높으면
        if i > mid:
            # 자른 나머지만큼 집으로 들고간다
            wood += i - mid

    # 가져가려는 나무와 들고 갈 나무의 개수가 같다면 바로 출력
    if wood == M:
        print(mid)
        exit()

    # 들고 갈 나무가 더 많다면 리스트에 저장 후 bottom 값 변경
    elif wood > M:
        possible.append(mid)
        bottom = mid + 1

    # 가져가야하는 나무가 더 많다면 top 값 변경
    elif wood < M:
        top = mid - 1

# 끝까지 정확한 나무 개수를 못찾았다면 담아갈 리스트에서 최댓값 출력
print(max(possible))

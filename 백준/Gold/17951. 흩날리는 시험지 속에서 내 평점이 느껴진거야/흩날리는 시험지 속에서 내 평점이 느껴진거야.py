# 이분 탐색 함수
def binary_search(left, right):
    while left <= right:
        mid = (left + right) // 2
        groups = [0] * K
        group_idx = 0

        for score in scores:
            if K == group_idx:
                break
            groups[group_idx] += score
            if groups[group_idx] > mid:
                group_idx += 1

        if group_idx < K:
            right = mid - 1
        else:
            left = mid + 1

    return left

# 입력 받기
N, K = map(int, input().split())
scores = list(map(int, input().split()))

# 이분 탐색을 사용하여 최적의 답 찾기
left, right = max(scores), sum(scores)
answer = binary_search(left, right)

print(answer)
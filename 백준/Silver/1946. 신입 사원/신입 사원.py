import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 서류 심사 성적별로 정렬
    arr = list(sorted([list(map(int, input().split())) for _ in range(N)]))
    # 임시로 설정한 최대 면접 성적
    top = arr[0][1]
    # 서류 심사 순위별 순회
    for i in arr:
        # 더 낮은 성적인 사람은 탈락
        if top < i[1]:
            N -= 1
        # 더 높은 성적이면 최대 면접 성적 변경
        else:
            top = i[1]

    print(N)
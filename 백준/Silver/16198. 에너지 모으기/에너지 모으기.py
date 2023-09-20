def back(n, cnt):
    global answer
    # 구슬이 2개만 남은 경우 에너지 최댓값 갱신 후 리턴
    if n == 2:
        answer = max(answer, cnt)
        return
    # 첫 구슬과 마지막 구슬 제외
    for i in range(1, len(arr) - 1):
        if not visited[i]:
            # 에너지의 합
            hap = arr[i - 1] * arr[i + 1]
            tmp = arr.pop(i)
            back(n - 1, cnt + hap)
            arr.insert(i, tmp)

N = int(input())
arr = list(map(int, input().split()))
visited = [False] * N
answer = 0
back(N, 0)
print(answer)
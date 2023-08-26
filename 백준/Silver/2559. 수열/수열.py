N, K = map(int, input().split())
arr = list(map(int, input().split()))
# K 일간 온도의 합
answer = 0
cnt = 0
for i in range(N):
    # M 일 이전까지는 현재 온도의 합과 정답에 더한다
    if i < K:
        cnt += arr[i]
        answer += arr[i]
    # M 일 이후
    else:
        # cnt 는 현재 온도의 합 갱신
        cnt += arr[i] - arr[i - K]
        # 정답보다 더 큰 온도의 합이 나오면 갱신
        if answer < cnt:
            answer = cnt

print(answer)
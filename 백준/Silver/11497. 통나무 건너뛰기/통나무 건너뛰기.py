T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(sorted(map(int, input().split())))
    stack = []
    answer = 0
    # 짝수번째 요소 순서대로 먼저 넣기
    for i in range(N):
        if i % 2 == 0:
            stack.append(arr[i])
    # 뒤에서부터 홀수번째 요소 넣기
    for i in range(N - 1, - 1, - 1):
        if i % 2 == 1:
            stack.append(arr[i])
    # 재구성된 리스트의 차 중 가장 큰 값을 출력
    for i in range(N - 1):
        answer = max(answer, abs(stack[i] - stack[i + 1]))

    print(answer)

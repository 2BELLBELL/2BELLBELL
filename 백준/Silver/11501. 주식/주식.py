T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 역순으로 탐색하기 위해 뒤집는다
    arr = list(map(int, input().split()))
    arr.reverse()
    # 현재 금액
    money = 0
    max_idx = arr[0]

    # 더 큰값이 들어오면 교체
    for i in arr:
        if i > max_idx:
            max_idx = i
        # 아니면 뺀 값을 돈에 더한다
        else:
            money += max_idx - i

    print(money)
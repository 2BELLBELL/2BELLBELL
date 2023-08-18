T = int(input())

for _ in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # 큐에 인덱스랑 함께 채워넣기
    q = []
    for idx, v in enumerate(arr):
        q.append([v, idx])

    cnt = 1
    while True:
        if q[0][0] == max(q)[0]:
            if q[0][1] == M:
                print(cnt)
                break
            else:
                q.pop(0)
                cnt += 1
        else:
            q.append(q.pop(0))
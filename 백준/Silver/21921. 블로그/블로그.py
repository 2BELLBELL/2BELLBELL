N, X = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
max_cnt = 0
max_idx = 0
for i in range(N):
    if i < X:
       cnt += arr[i]
       if cnt > max_cnt:
           max_cnt = cnt
           max_idx = 1
       elif cnt == max_cnt:
           max_idx += 1
    else:
        cnt = cnt - arr[i - X] + arr[i]
        if cnt > max_cnt:
            max_cnt = cnt
            max_idx = 1
        elif cnt == max_cnt:
            max_idx += 1

if max_cnt == 0:
    print('SAD')
else:
    print(max_cnt)
    print(max_idx)
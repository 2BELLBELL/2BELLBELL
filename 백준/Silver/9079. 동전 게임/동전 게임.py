from collections import deque

def change(num):
    if num == 1:
        return 0
    else:
        return 1

def bfs(arr, act_num):
    q = deque([[arr, act_num, 0]])
    while True:
        tmp_arr, tmp_act_num, cnt = q.popleft()
        if tmp_arr == [0, 0, 0, 0, 0, 0, 0, 0, 0] or tmp_arr == [1, 1, 1, 1, 1, 1, 1, 1, 1]:
            print(cnt)
            return
        if cnt > 5:
            print(-1)
            return

        # 가로 경우의 수
        if tmp_act_num != 1:
            tmp1 = tmp_arr[:]
            tmp1[0] = change(tmp1[0])
            tmp1[1] = change(tmp1[1])
            tmp1[2] = change(tmp1[2])
            q.append([tmp1, 1, cnt+1])
        if tmp_act_num != 2:
            tmp2 = tmp_arr[:]
            tmp2[3] = change(tmp2[3])
            tmp2[4] = change(tmp2[4])
            tmp2[5] = change(tmp2[5])
            q.append([tmp2, 2, cnt+1])
        if tmp_act_num != 3:
            tmp3 = tmp_arr[:]
            tmp3[6] = change(tmp3[6])
            tmp3[7] = change(tmp3[7])
            tmp3[8] = change(tmp3[8])
            q.append([tmp3, 3, cnt+1])
        # 세로 경우의 수
        if tmp_act_num != 4:
            tmp4 = tmp_arr[:]
            tmp4[0] = change(tmp4[0])
            tmp4[3] = change(tmp4[3])
            tmp4[6] = change(tmp4[6])
            q.append([tmp4, 4, cnt+1])
        if tmp_act_num != 5:
            tmp5 = tmp_arr[:]
            tmp5[1] = change(tmp5[1])
            tmp5[4] = change(tmp5[4])
            tmp5[7] = change(tmp5[7])
            q.append([tmp5, 5, cnt+1])
        if tmp_act_num != 6:
            tmp6 = tmp_arr[:]
            tmp6[2] = change(tmp6[2])
            tmp6[5] = change(tmp6[5])
            tmp6[8] = change(tmp6[8])
            q.append([tmp6, 6, cnt+1])
        # 대각선 경우의 수
        if tmp_act_num != 7:
            tmp7 = tmp_arr[:]
            tmp7[0] = change(tmp7[0])
            tmp7[4] = change(tmp7[4])
            tmp7[8] = change(tmp7[8])
            q.append([tmp7, 7, cnt+1])
        if tmp_act_num != 8:
            tmp8 = tmp_arr[:]
            tmp8[2] = change(tmp8[2])
            tmp8[4] = change(tmp8[4])
            tmp8[6] = change(tmp8[6])
            q.append([tmp8, 8, cnt+1])

T = int(input())
for tc in range(1, T + 1):
    arr = []
    for _ in range(3):
        tmp = list(input().split())
        for i in range(3):
            if tmp[i] == 'T':
                tmp[i] = 0
            else:
                tmp[i] = 1
        arr.extend(tmp)
    bfs(arr, 0)
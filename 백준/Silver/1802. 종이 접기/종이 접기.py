T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input()))
    result = 'YES'
    mid = len(arr) // 2
    while mid != 0:
        # 좌우가 대칭인지 확인
        flag = True
        for i in range(mid):
            if arr[i] + arr[-1 - i] != 1:
                flag = False
        # 대칭이 아니라면 NO 출력
        if not flag:
            result = 'NO'
            break
        else:
            # 대칭인 경우 arr 재설정 후 반복
            arr = arr[:mid]
            mid //= 2

    print(result)
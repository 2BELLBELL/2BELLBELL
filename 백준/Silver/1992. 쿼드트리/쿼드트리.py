def cut(x, y, cnt):
    # 색종이의 합을 구한다
    hap = 0
    for i in range(x, x + cnt):
        for j in range(y, y + cnt):
            hap += arr[i][j]

    # 잘라진 색종이가 하얀색이면
    if hap == 0:
        print('0', end='')
        return
    # 잘라진 색종이가 파란색이면
    elif hap == cnt ** 2:
        print('1', end='')
        return
    # 색종이를 더 잘라야 하는 경우
    else:
        print('(', end='')
        for i in range(x, x + cnt, cnt // 2):
            for j in range(y, y + cnt, cnt // 2):
                cut(i, j, cnt // 2)
    print(')', end='')
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
cut(0, 0, N)
def Z(n, x, y, max_cnt, min_cnt):
    if n == 1:
        if x == 1 and y == 1:
            print(int(min_cnt) + 3)
        elif x == 1 and y == 0:
            print(int(min_cnt) + 2)
        elif x == 0 and y == 1:
            print(int(min_cnt) + 1)
        elif x == 0 and y == 0:
            print(int(min_cnt))
        exit()

    if x >= 2 ** (n - 1):
        if y >= 2 ** (n - 1):
            min_cnt += (max_cnt - min_cnt) * 0.75
        else:
            a = max_cnt - (max_cnt - min_cnt) * 0.25
            b = (max_cnt + min_cnt) // 2
            max_cnt, min_cnt = a, b
    elif x < 2 ** (n - 1):
        if y < 2 ** (n - 1):
            max_cnt -= (max_cnt - min_cnt) * 0.75
        else:
            a = (max_cnt + min_cnt) // 2
            b = min_cnt + (max_cnt - min_cnt) * 0.25
            max_cnt, min_cnt = a, b

    Z(n - 1, x % (2 ** (n-1)), y % (2 ** (n-1)), max_cnt, min_cnt)

N, r, c = map(int, input().split())
min_num = 0
max_num = 2 ** N * 2 ** N
Z(N, r, c, max_num, min_num)
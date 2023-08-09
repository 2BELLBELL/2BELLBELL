# 4개의 각 줄을 시행
for _ in range(4):
    # 1번 직사각형의 좌표 (x1,y1) (x2,y2)
    # 2번 직사각형의 좌표 (i1,j1) (i2,j2)
    x1, y1, x2, y2, i1, j1, i2, j2 = map(int, input().split())

    # 겹치는 부분이 점이 되는 경우
    # 1) 1번 직사각형 우상단과 2번 직사각형 좌하단
    if x2 == i1 and y2 == j1:
        print('c')
    # 2) 2번 직사각형 우상단과 1번 직사각형 좌하단
    elif i2 == x1 and j2 == y1:
        print('c')
    # 3) 1번 직사각형 좌상단과 2번 직사각형 우하단
    elif x1 == i2 and y2 == j1:
        print('c')
    # 4) 2번 직사각형 좌상단과 1번 직사각형 우하단
    elif i1 == x2 and j2 == y1:
        print('c')

    # 겹치는 부분이 선분이 되는 경우
    # (점이 될 수 있는 경우는 if 문이 여기까지 안옴)
    # 1) 1번 직사각형 상단과 2번 직사각형 하단
    elif y2 == j1 and x1 <= i1 <= x2:
        print('b')
    elif y2 == j1 and x1 <= i2 <= x2:
        print('b')
    elif y2 == j1 and i1 <= x1 <= i2:
        print('b')
    elif y2 == j1 and i1 <= x2 <= i2:
        print('b')
    # 2) 2번 직사각형 상단과 1번 직사각형 하단
    elif j2 == y1 and i1 <= x1 <= i2:
        print('b')
    elif j2 == y1 and i1 <= x2 <= i2:
        print('b')
    elif j2 == y1 and x1 <= i1 <= x2:
        print('b')
    elif j2 == y1 and x1 <= i2 <= x2:
        print('b')
    # 3) 1번 직사각형 우변과 2번 직사각형 좌변
    elif x2 == i1 and y1 <= j1 <= y2:
        print('b')
    elif x2 == i1 and y1 <= j2 <= y2:
        print('b')
    elif x2 == i1 and j1 <= y1 <= j2:
        print('b')
    elif x2 == i1 and j1 <= y2 <= j2:
        print('b')
    # 4) 2번 직사각형 우변과 1번 직사각형 좌변
    elif i2 == x1 and j1 <= y1 <= j2:
        print('b')
    elif i2 == x1 and j1 <= y2 <= j2:
        print('b')
    elif i2 == x1 and y1 <= j1 <= y2:
        print('b')
    elif i2 == x1 and y1 <= j2 <= y2:
        print('b')

    # 각 직사각형의 공통부분이 없는 경우
    # (점이나 선분이 될 수 있는 경우는 if 문이 여기까지 안옴)
    # 1) 1번 직사각형이 더 위쪽에 있는 경우
    elif j2 <= y1:
        print('d')
    # 2) 2번 직사각형이 더 위쪽에 있는 경우
    elif y2 <= j1:
        print('d')
    # 3) 1번 직사각형이 더 왼쪽에 있는 경우
    elif x2 <= i1:
        print('d')
    # 4) 2번 직사각형이 더 위쪽에 있는 경우
    elif i2 <= x1:
        print('d')

    # 모든 분기를 지났다... 이젠 직사각형이 겹칠 때 뿐
    # 그 외에 직사각형 겹칠 때
    else:
        print('a')
from collections import deque

# 로봇 방향 전환 함수
def rotation(v, rot):
    di = deque(['N', 'W', 'S', 'E'])
    for i in range(4):
        if di[i] == v:
            idx = i
            break
    di.rotate(rot)
    return di[idx]

# 로봇 전진 함수
def go(x, y, dis, cnt):
    if dis == 'N':
        y += 1
    elif dis == 'S':
        y -= 1
    elif dis == 'W':
        x -= 1
    elif dis == 'E':
        x += 1

    if x > A or x < 1 or y > B or y < 1:
        print(f'Robot {cnt} crashes into the wall')
        exit()
    for i in range(1, len(robot)):
        if robot[i][0] == x and robot[i][1] == y:
            print(f'Robot {cnt} crashes into robot {i}')
            exit()
    return (x, y)

A, B = map(int, input().split())
N, M = map(int, input().split())
robot = [[False]]
# 로봇의 초기 위치와 방향 입력 받기
for _ in range(N):
    x, y, dir = input().split()
    robot.append([int(x), int(y), dir])

# 각각의 명령 입력 받기
for _ in range(M):
    num, order, repeat = input().split()
    # 좌측으로 방향 전환
    if order == 'L':
        for i in range(int(repeat)):
            robot[int(num)][2] = rotation(robot[int(num)][2], -1)
    # 우측으로 방향 전환
    elif order == 'R':
        for i in range(int(repeat)):
            robot[int(num)][2] = rotation(robot[int(num)][2], 1)
    # 전진
    elif order == 'F':
        for i in range(int(repeat)):
            robot[int(num)][0], robot[int(num)][1] = go(*robot[int(num)], num)

print('OK')
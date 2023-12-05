from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1] 

direction = {
    1: [[0], [1], [2], [3]],            # 1번cctv 방향:0, 1, 2, 3, --> 4가지
    2: [[0, 2], [1, 3]],                    # 2번cctv 방향:(0, 2), (1, 3) --> 2가지
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],    # 3번cctv 방향:(0, 1), (1, 2), (2, 3), (3, 0) --> 4가지
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],    # 4번cctv 방향... 4가지
    5: [[0, 1, 2, 3]]                      # 5번cctv 방향... 1가지
}

def check(row, col):
    return row < 0 or row >=N or col < 0 or col >=M
    

def init():
    obj = deque() #  cctv의 위치를 저장할 큐 
    answer = 0
    for i in range(N):
        for j in range(M):
            # 벽이아니고 빈칸이아니면 
            if space[i][j] != 6 and space[i][j] != 0:
                obj.append((space[i][j], i, j))   # cctv번호, cctv 좌표 저장
            # cctv가 아에 없는 경우도 고려해서 빈칸의 갯수로 맞춰둠
            if space[i][j] == 0:answer += 1
    return obj, answer

# cctv좌표들, 빈칸 개수 초기화
cctv, answer = init()


def move(y, x, direc, space_copy):
    # 각각의 방향에 대해서 전부 이동시켜줌
    for d in direc:
        ny, nx = y, x
        
        while True:
            nx += dx[d]
            ny += dy[d]
            if check(ny, nx) or space_copy[ny][nx] == 6:
                break
            # 빈칸이아니면 
            if space_copy[ny][nx] != 0:
                continue
            space_copy[ny][nx] = '#'

    
def zero_cnt(space_copy):
    global answer
    cnt = 0
    for i in space_copy:
        cnt += i.count(0)
    answer = min(answer, cnt) 
    

def dfs(level, space):
    # space_copy = copy.deepcopy(space)           
    space_copy = [[j for j in space[i]] for i in range(N)]
   
    if level == len(cctv):
        zero_cnt(space_copy)
        return
    
    number, y, x  = cctv[level]
    

    for d in direction[number]:    
        move(y, x, d, space_copy)
        dfs(level+1, space_copy)
        space_copy = [[j for j in space[i]] for i in range(N)]
    
dfs(0, space)
print(answer)
import sys
# input = sys.stdin.readline  
# sys.stdin = open('input.txt')
# import numpy as np
# from itertools import combinations
from collections import deque

'''
deque를 활용하여 인덱스기준 2, 6만 확인한다.
dfs로 양쪽으로 쭉쭉 밀기
'''


def dfs(n, d):
    # 현재 톱니바퀴 회전
    # print(f'현재 톱니바퀴: {n + 1}, 회전방향: {d}')
    # print(np.array(gear))


    # 왼쪽 톱니바퀴 확인
    if n != 0 and not visited[n - 1] and gear[n][6] != gear[n - 1][2]:
        visited[n - 1] = True
        dfs(n - 1, -d)
    # 오른쪽 톱니바퀴 확인
    if n != 3 and not visited[n + 1] and gear[n][2] != gear[n + 1][6]:
        visited[n + 1] = True
        dfs(n + 1, -d)
    gear[n].rotate(d)

# 12시부터 시계방향으로 N극은 0, S극은 1
gear = [deque(list(map(int, input()))) for _ in range(4)]
# 회전의 총 횟수
spin_cnt = int(input())
# 톱니번호, 방향(1은 시계, -1은 반시계)
for _ in range(spin_cnt):
    number, direction = map(int, input().split())
    # 인덱스 접근용으로 -1 빼기
    number -= 1
    visited = [False] * 4
    visited[number] = True
    dfs(number, direction)

answer = 0
cnt = 1
for i in range(4):
    if gear[i][0]:
        answer += cnt
    cnt *= 2

print(answer)
import sys

# 좌표를 입력 받는다
x, y, w, h = map(int, sys.stdin.readline().split())

# 최대 거리 임의 설정
distance = 1000

# 직사각형 경계까지 가는 최솟값 확인
if x < distance:
    distance = x
if y < distance:
    distance = y
if w - x < distance:
    distance = w - x
if h - y < distance:
    distance = h - y

print(distance)
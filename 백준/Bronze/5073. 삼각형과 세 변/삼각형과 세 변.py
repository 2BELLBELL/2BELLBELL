import sys

while True:
    # 세 변의 길이를 입력 받는다
    x, y, z = map(int, sys.stdin.readline().split())

    # 0, 0, 0 이 나오면 탈출
    if sum([x, y, z]) == 0:
        break

    # 모든 변의 길이가 같을 때
    elif x == y == z:
        print('Equilateral')

    # 가장 긴 변이 나머지 변 두개를 합친 것보다 길면
    elif max(x, y, z) >= sum([x, y, z]) - max(x, y, z):
        print('Invalid')

    # 세 변의 길이가 모두 다를 때
    elif x != y and x != z and y != z:
        print('Scalene')

    # 그 외 두 변의 길이만 같을 때
    else:
        print('Isosceles')
import sys

# 세 각의 크기를 각각 입력 받는다
x = int(sys.stdin.readline())
y = int(sys.stdin.readline())
z = int(sys.stdin.readline())

# 세 각의 합이 180이 아닌 경우
if x + y + z != 180:
    print('Error')
# 세 각의 합이 180이고 모든 각이 같을 때
elif x == y == z:
    print('Equilateral')
# 세 각의 합이 180이고 모든 각이 다를 때
elif x != y and x != z and y != z:
    print('Scalene')
# 세 각의 합이 180이고 그 외
else:
    print('Isosceles')
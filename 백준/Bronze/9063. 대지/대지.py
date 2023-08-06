import sys
x_lst = []
y_lst = []
N = int(sys.stdin.readline())

# 각각의 x좌표와 y좌표를 리스트에 삽입한다 
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    x_lst.append(x)
    y_lst.append(y)

# (x좌표의 최댓값 - 최솟값) * (y좌표의 최댓값 - 최솟값) 출력
print((max(x_lst)-min(x_lst)) * (max(y_lst)-min(y_lst)))
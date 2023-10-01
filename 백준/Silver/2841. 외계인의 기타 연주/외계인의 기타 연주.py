import sys

n, p = map(int, sys.stdin.readline().split())
line = [[0] for x in range(7)]
cnt = 0

# 반복문을 통해 줄의 번호와 프렛의 번호를 확인
for i in range(n):
    line_num, plat_num = map(int, sys.stdin.readline().split())

    # 주어진 줄의 더 높은 프렛을 누르고 있는 경우, 손가락을 하나씩 뗀다.
    while line[line_num][-1] > plat_num:
        line[line_num].pop()
        cnt += 1

    # 이미 누르고 있는 줄의 프렛인 경우 패스
    if line[line_num][-1] == plat_num:
        continue

    # 주어진 줄의 프렛을 누른다.
    line[line_num].append(plat_num)
    cnt += 1

print(cnt)
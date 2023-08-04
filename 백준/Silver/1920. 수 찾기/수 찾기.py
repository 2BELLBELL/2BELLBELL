import sys

# 입력 값 생성
N = sys.stdin.readline()
A = set(map(int, sys.stdin.readline().split()))
M = sys.stdin.readline()
M_list = list(map(int, sys.stdin.readline().split()))

for i in M_list:
    if i in A:
        print(1)
    else:
        print(0)
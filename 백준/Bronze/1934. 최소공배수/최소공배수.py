import sys

T = int(sys.stdin.readline())

for i in range(1, T + 1):
    A,B = map(int,input().split())
    a = A
    b = B
    n = 1
    while n != 0:
        n = a % b
        a = b
        b = n

    print(int(A*B/a))
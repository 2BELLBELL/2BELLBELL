import sys
T = int(sys.stdin.readline())
for i in range(1, T + 1):
    # 받을 돈 변수 생성
    money = int(input())
    # 주어진 돈의 단위 변수 * 100
    Q = 0
    D = 0
    N = 0
    P = 0

    # 쿼터에 25로 나눈 몫을 더하고
    Q += money // 25
    # 몫 * 25 만큼 돈에서 뺀다
    money -= Q * 25

    # 다임에 10으로 나눈 몫을 더하고
    D += money // 10
    # 몫 * 10 만큼 돈에서 뺀다
    money -= D * 10

    # 니켈에 5로 나눈 몫을 더하고
    N += money // 5
    # 몫 * 5 만큼 돈에서 뺀다
    money -= N * 5

    # 페니에 1로 나눈 몫을 더하고
    P += money // 1
    # 몫 * 1 만큼 돈에서 뺀다
    money -= P * 1

    print(Q, D, N, P)
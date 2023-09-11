N, K = map(int, input().split())
bag = [0] * (K + 1)
for _ in range(N):
    W, V = map(int, input().split())
    for i in range(K, W - 1, - 1):
        bag[i] = max(bag[i], bag[i - W] + V)
    # 정순으로 탐색 시, 이미 변경된 값을 참조하기 때문에 반복 참조 불가하도록 역순으로 돌아야함
    # for i in range(W, K + 1):
    #     bag[i] = max(bag[i], bag[i - W] + V)
print(max(bag))

# 무게 0  1  2  3  4  5  6   7
#    [0, 0, 0, 0, 0, 0, 13, 13]
#    [0, 0, 0, 0, 8, 8, 13, 13]
#    [0, 0, 0, 6, 8, 8, 13, 14]
#    [0, 0, 0, 6, 8, 12, 13, 14]
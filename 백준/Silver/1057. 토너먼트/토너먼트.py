N, KIM, LIM = map(int, input().split())
ROUND = 0
while KIM != LIM:
    KIM, LIM = (KIM + 1) // 2, (LIM + 1) // 2
    ROUND += 1
print(ROUND)
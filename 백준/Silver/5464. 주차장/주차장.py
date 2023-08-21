import sys

N, M = map(int, sys.stdin.readline().split())
q = [0] * N
weiting = []
price = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
weight = [int(sys.stdin.readline().rstrip()) for _ in range(M)]
cnt = 0

for i in range(2*M):
    parking = int(sys.stdin.readline().rstrip())
    if parking > 0:
        for i in range(N):
            if q[i] == 0:
                q[i] = parking
                cnt += price[i] * weight[parking-1]
                break
        else:
            weiting.append(parking)
    elif parking < 0:
        for i in range(N):
            if q[i] + parking == 0:
                q[i] = 0
                break
        if len(weiting) != 0:
            q[i] = weiting.pop(0)
            cnt += price[i] * weight[q[i]-1]
print(cnt)
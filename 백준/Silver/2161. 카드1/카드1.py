N = int(input())
q = list(range(1, N+1)) * (N+1)
# 선형 큐 활용
front = 0
rear = N-1

for _ in range(N):
    print(q[front], end=' ')
    front += 2
    rear += 1
    q[rear] = q[front-1]
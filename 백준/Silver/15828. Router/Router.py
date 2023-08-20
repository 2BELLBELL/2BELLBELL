import sys

N = int(sys.stdin.readline().rstrip())
q = []
front = 0
rear = 0

# 패킷 정보 처리
while True:
    order = int(sys.stdin.readline().rstrip())
    # 입력의 종료 조건
    if order == -1:
        break
    # 0이 아닌 경우 버퍼의 크기보다 작으면 큐에 넣고 rear + 1 
    if order != 0:
        if rear - front < N:
            q.append(order)
            rear += 1
    # 0인 경우 하나 처리 (front + 1)
    elif order == 0:
        front += 1

# 큐가 비어있는 경우
if front == rear:
    print('empty')

# 큐가 비어 있지 않은 경우 front 부터 rear 까지 순서대로 출력
while front != rear:
    print(q[front], end=' ')
    front += 1


import sys

N = int(sys.stdin.readline().rstrip())
q = [0] * 10001
front = rear = -1

for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        rear += 1
        q[rear] = int(order[1])
    elif order[0] == 'front':
        if q[front+1] != 0:
            print(q[front+1])
        else:
            print(-1)
    elif order[0] == 'back':
        if q[rear] != 0 and rear != front:
            print(q[rear])
        else:
            print(-1)
    elif order[0] == 'pop':
        if q[front+1] != 0:
            front += 1
            print(q[front])
        else:
            print(-1)
    elif order[0] == 'size':
        print(rear - front)
    elif order[0] == 'empty':
        if rear == front:
            print(1)
        else:
            print(0)
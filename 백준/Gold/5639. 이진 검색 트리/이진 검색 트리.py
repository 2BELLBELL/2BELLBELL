import sys
sys.setrecursionlimit(10**9)

arr = []
while True:
    try:
        arr.append(int(sys.stdin.readline().rstrip()))
    except:
        break

def postorder(left, right):
    if left > right:
        return
    else:
        mid = right + 1
        for i in range(left + 1, right + 1):
            # 해당 원소가 현재 노드보다 크다면 그 전까지는 왼쪽 서브 트리,
            # 해당 원소 이후는 오른쪽 서브 트리이다.
            if arr[left] < arr[i]:
                mid = i
                break
        postorder(left+1, mid-1)
        postorder(mid, right)
        print(arr[left])

postorder(0, len(arr)-1)
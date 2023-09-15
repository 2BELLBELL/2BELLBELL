import sys
input = sys.stdin.readline

N = int(input())
heap = [None]
for _ in range(1, N + 1):
    num = int(input())
    # 힙에서 큰 값을 출력하고 배열에서 제거하는 경우
    if num == 0:
        # 힙이 비어있는 경우
        if len(heap) == 1:
            print(0)
        # 힙이 차있는 경우
        else:
            # 힙의 첫번쨰 요소를 마지막 요소랑 바꾸고 출력
            heap[1], heap[-1] = heap[-1], heap[1]
            print(heap.pop())
            # 힙 재정렬
            idx = 1
            while True:
                child_idx = 0
                # 두 자식 다 있으면
                if len(heap) - 1 >= idx * 2 + 1:
                    # 왼쪽, 오른쪽 자식 비교
                    if heap[idx * 2] > heap[idx * 2 + 1]:
                        child_idx = idx * 2
                    else:
                        child_idx = idx * 2 + 1

                # 왼쪽 자식만 있으면
                elif len(heap) - 1 == idx * 2:
                    child_idx = idx * 2

                # 두 자식 다 없으면
                else:
                    break

                # 부모, 자식 비교 후 자리교체
                if heap[idx] >= heap[child_idx]:
                    break
                else:
                    heap[idx], heap[child_idx] = heap[child_idx], heap[idx]
                    idx = child_idx
    # 힙에 요소를 삽입하는 경우
    else:
        # 힙의 마지막 요소로 삽입
        heap.append(num)
        # 마지막 요소의 현재 인덱스
        idx = len(heap) - 1
        # 부모보다 작은 숫자거나 인덱스가 1이 될때까지 반복
        while idx != 1 and heap[idx] > heap[idx//2]:
            heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
            idx //= 2
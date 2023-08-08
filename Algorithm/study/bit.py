arr = ['Fish', 'And', 'Chip']
N = len(arr)

for i in range(1 << N):       # 부분 집합의 개수 (8이 들어가고)
    for j in range(N):     # 원소의 수만큼 비트를 비교 (3이 들어가지)
        if i & (1 << j):      # i의 j번 비트가 1인 경우
            print(arr[j], end=' ')      # j번 원소 출력
    print()
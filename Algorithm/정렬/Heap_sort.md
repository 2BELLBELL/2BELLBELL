# 힙 정렬

### 힙이란
- 최대 힙이나 최소 힙을 구성해 정렬을 하는 방법
- 불안정 정렬인 이유: 최댓값은 확실하나 같은 층의 숫자끼리는 정렬되어 있지 않아서
- 시간복잡도 : O(nlogn)

- 부모 노드와 자식 노드로

### 부모 노드와 자식 노드의 관계

![힙 노드 한눈에](https://i.imgur.com/3sUWVY2.png)

### 내림차순 '최대 힙'과 오름차순 '최소 힙'

![힙 종류](https://gmlwjd9405.github.io/images/data-structure-heap/types-of-heap.png)

### 힙의 단계
1. 분할(Divide): 정렬되지 않은 배열을 반으로 분할합니다.
2. 정복(Conquer): 각각의 부분 배열을 재귀적으로 병합 정렬합니다.
3. 결합(Combine): 정렬된 두 개의 부분 배열을 하나의 정렬된 배열로 병합합니다.

### 최소 힙 구조 만들기


```python
def heapify(li, idx, n):
    # li : 힙으로 만들고자 하는 배열
    # idx : 선택된 노드
    # n : 힙의 범위

    # 자식의 왼쪽 노드를 의미
    left = idx * 2
    # 자식의 오른쪽 노드를 의미
    right = idx * 2 + 1
    s_idx = idx

    # 선택 노드, 선택 노드의 양 자식 중 가장 작은 값을 찾는 과정
    if left <= n and li[s_idx] > li[left]:
        s_idx = left
    if right <= n and li[s_idx] > li[right]:
        s_idx = right

    # 선택 노드와 자식 노드의 위치가 바뀌어야 한다면
    if s_idx != idx:
        # 부모 자식 위치 변경
        li[idx], li[s_idx] = li[s_idx], li[idx]
        # 부모가 자식으로 내려간 이후에도, 그 자식과 바뀔 여지가 있는지 재귀로 체크
        return heapify(li, s_idx, n)
```

### 최소 힙 정렬 실행


```python
def heap_sort(array):
    n = len(array)

    # 루트노드는 index 1부터 시작하므로, 앞에 0 원소를 추가한 채로 시작.
    array = [0] + array

    # 최종 정렬된 원소들이 저장될 배열
    ans = []

    # Min Heap을 만드는 과정
    for i in range(n // 2, 0, -1):
        heapify(array, i, n)

    # 루트 노드 원소를 정렬 배열에 저장, heapify 반복
    for i in range(n, 0, -1):
        ans.append(array[1])
        array[i], array[1] = array[1], array[i]
        heapify(array, 1, i - 1)

    # array[1:]를 얻으면 오름차순 정렬 배열을 얻을 수 있음
    return ans
```

![예제 2](https://blog.kakaocdn.net/dn/bzfBwF/btqFOM16NBX/AlAJkIe4uwtXHd6hThT7Kk/img.gif)


```python
print(heap_sort([3, 4, 5, 2, 1, 6, 7]))
```

    [1, 2, 3, 4, 5, 6, 7]
    

### 장점
- 안정적인 성능(최악/평균/최선 성능이 동일)
- 추가적인 메모리 공간 사용 X

### 단점
- 구현이 복잡한데 평균점으로 퀵 정렬보다 느려서 실제로 활용되지 않음
    - 참조 지역성 원리 : 힙 정렬은 트리로 구성된 것을 전제로 하기 때문에 원소를 임의 접근하는 반면, 퀵 정렬은 인접한 원소를 접근하는 방식으로 전개되어 실제론 힙 정렬보다 빠른 처리 속도

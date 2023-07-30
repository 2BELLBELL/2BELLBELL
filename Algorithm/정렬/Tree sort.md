# 트리의 구조

**노드(Node), 키(Key)**

![image-20230729081037840](C:\Users\lyj00\AppData\Roaming\Typora\typora-user-images\image-20230729081037840.png)

- 트리를 구성하는 하나의 요소를 노드라고 부르며 하나의 노드가 저장하는 값을 키라고 함

- 하나의 노드는 키와 자손을 가리키는 참조 변수(left, right)를 가짐
- n개의 노드가 있을 때 간선의 수는 n - 1



**루트노드(Root Node), 서브 트리(Subtree)**

![image-20230729081229099](C:\Users\lyj00\AppData\Roaming\Typora\typora-user-images\image-20230729081229099.png)

- 가장 낮은 높이에 존재하는 노드를 루트 노드라고 함
- 해당 노드의 왼쪽 혹은 오른쪽에 있는 노드들을 묶으면 하나의 트리 형태가 되는데, 이를 서브 트리라고 함



**트리의 높이, 노드의 레벨**

![image-20230729081254658](C:\Users\lyj00\AppData\Roaming\Typora\typora-user-images\image-20230729081254658.png)

- 노드의 레벨은 루트 노드가 레벨 0에서 시작하여 자식 노드로 내려갈수록 레벨이 1씩 증가
- 경우에 따라 루트 노드의 레벨을 1로 보는 경우도 있으며 단지 초기 레벨 설정의 차이
- 트리의 높이는 레벨이 가장 높은 노드의 레벨 



**부모 노드, 형제 노드, 조상 노드**

![image-20230729081948224](C:\Users\lyj00\AppData\Roaming\Typora\typora-user-images\image-20230729081948224.png)

- 해당 노드 기준으로 바로 위의 레벨에 있는 노드를 부모 노드
- 같은 레벨에 있는 노드를 형제 노드
- 아래 레벨에 있는 노드를 자식 노드
- 바로 위는 아니지만 위에 있는 노드를 조상 노드
- 바로 아래는 아니지만 아래 레벨에 있는 노드를 후손 노드



**단말 노드(Leaf node), 내부 노드(Internal node)**

![image-20230729082148760](C:\Users\lyj00\AppData\Roaming\Typora\typora-user-images\image-20230729082148760.png)

- 자손을 가지지 않는 노드를 단말 노드
- 자손을 가지는 노드를 내부 노드



# 이진 트리 (Binary tree)

: 뿌리 트리에서 자식 노드가 2개 이하인 트리 (= 모든 노드의 차수가 2 이하)

- 0개 이상의 노드들로 이루어진 유한 집합
- 공집합이거나 뿌리의 왼쪽 부분 트리와 오른쪽 부분 트리로 구성
- 모든 노드가 2개의 부분 트리르 가지고 있는 트리 (부분 트리는 공집합일 수 있음)



**이진 트리의 유용한 성질**

![image-20230729082851488](C:\Users\lyj00\AppData\Roaming\Typora\typora-user-images\image-20230729082851488.png)

- 레벨 k에서 가질 수 있는 최대 노드 수: 2^k
- 높이가 m인 이진 트리가 가질  수 있는 최대 노드 수: 2^m+1 - 1
- 높이가 m인 이진 트리가 가질 수 있는 최소 노드 수: m + 1



# 이진 트리의 배열 표현

- 형제 노드 중 왼쪽 노드의 인덱스 순서가 오른쪽 노드보다 빠름
- 노드 번호는 1부터 시적하며 인덱스 0번은 비워 둠



![image-20230729083854130](C:\Users\lyj00\AppData\Roaming\Typora\typora-user-images\image-20230729083854130.png)

- 루트 노드 = 1 (n > 0)
- 노드 i의 부모 노드 인덱스 = i / 2 (i > 1)
- 노드 i의 왼쪽 자식 노드 인덱스 = i * 2 (i * 2 <= n)
- 노드 i의 오른쪽 자식 노드 인덱스 = i * 2 + 1 (i * 2 + 1 <= n)

![image-20230729084117387](C:\Users\lyj00\AppData\Roaming\Typora\typora-user-images\image-20230729084117387.png)

- 배열을 사용하면 노드 접근이 빠르고 구현이 용이하다는 장점이 있지만, (1) 편향 이진 트리의 경우 많은 공간이 낭비될 수 있고 (2) 배열 크기 이상의 노드를 추가할 수 없음
  		- 연결 리스트 표현: 포인터를 사용하여 이진트리를 표현하면 배열보다는 접근 속도가 느리지만 삽입 및 삭제가 쉽고 노드를 포인터로 연결하기 때문에 노드 수에 제한이 없음 (파이썬 x)



# 이진 트리의 종류

## 편향 이진 트리

: 노드들이 한쪽으로 편향되어 있음

![image-20230729084731083](C:\Users\lyj00\AppData\Roaming\Typora\typora-user-images\image-20230729084731083.png)

**문제점**

1. 탐색 속도 저하: E를 탐색하기 위해 모든 노드를 탐색해야 함
2. 공간 낭비: 연결 리스트로 구현할 경우는 문제가 없지만 인덱스로 구현할 경우 노드 개수가 i라면 최대 2^i의 공간을 필요로 함



## 포화 이진 트리

: 높이가 h일 때 최대 노드의 수는 2(h+1) - 1개인데, 이때 이진 트리에서 최대 노드의 수를 만족하는 트리

![image-20230729084949892](C:\Users\lyj00\AppData\Roaming\Typora\typora-user-images\image-20230729084949892.png)



## 완전 이진 트리

: 높이가 h인 트리에서 노드 수가 n일 때 레벨 순서 번호가 1~n까지 모두 일치하는 트리. 즉, 왼쪽 노드부터 차례대로 키가 들어가 있음

![image-20230729085046749](C:\Users\lyj00\AppData\Roaming\Typora\typora-user-images\image-20230729085046749.png)



**왼전 이진 트리가 아닌 예**

![image-20230729085132758](C:\Users\lyj00\AppData\Roaming\Typora\typora-user-images\image-20230729085132758.png)



# 이진 탐색 트리 (BST, Binary Search Tree)

: 정렬된 이진 트리

- 노드의 왼쪽 하위 트리에는 노드의 키보다 작은 키가 있는 노드만 포함
- 노드의 오른쪽 하위 트리에는 노드의 키보다 큰 키가 있는 노드만 포함
- 왼쪽 및 오른쪽 하위 트리도 각각 이진 탐색 트리여야 함
- 중복 키를 허용하지 않음

![image-20230729085308256](C:\Users\lyj00\AppData\Roaming\Typora\typora-user-images\image-20230729085308256.png)

## 순회

### 전위 순회 (Preorder Traversal)

rood -> left -> right



### 중위 순회 (Inorder Traversal)

left -> root -> right



### 후위 순회 (Postorder Traversal)

left -> right -> root





## 삽입

![image-20230729085412223](C:\Users\lyj00\AppData\Roaming\Typora\typora-user-images\image-20230729085412223.png)

1. 50을 트리의 루트로 삽입
2. 다음 요소를 읽고 루드 노드 요소보다 작으면 왼쪽 하위 트리의 루트로 삽입
3. 그렇지 않으면 오른쪽 하위 트리의 오른쪽 루트로 삽입



## 검색

![image-20230729085723129](C:\Users\lyj00\AppData\Roaming\Typora\typora-user-images\image-20230729085723129.png)

1. 루트에서 시작
2. 검색 값을 루트와 비교하고 루트보다 작으면 왼쪽으로 재귀, 크다면 오른쪽으로 재귀
3. 검색 값이 없으면 null 반환

- BST의 검색에 대한 시간 복잡도는 균형 상태일 경우 O(logN), 불균형 상태일 경우 최대 O(N)



## 삽입

![image-20230729085840294](C:\Users\lyj00\AppData\Roaming\Typora\typora-user-images\image-20230729085840294.png)

1. 루트에서 시작
2. 삽입 값을 루트와 비교하고 루트보다 작으면 왼쪽으로 재귀, 크다면 오른쪽으로 재귀
3. 리프 노드에 도달한 후 노드보다 크다면 오른쪽에, 작다면 왼쪽에 삽입



## 삭제

**삭제할 노드가 리프노드인 경우**

- 노드를 삭제하기만 하면 됨

![image-20230729090158913](C:\Users\lyj00\AppData\Roaming\Typora\typora-user-images\image-20230729090158913.png)**삭제할 노드에 자식이 둘 있는 경우**

- 자식 둘 있는 경우 successor 노드를 찾는 과정이 추가됨

- successor 노드: 선택한 노드의 오른쪽 서브 트리 중 가장 작은 값을 가지는 노드

![image-20230729090504863](C:\Users\lyj00\AppData\Roaming\Typora\typora-user-images\image-20230729090504863.png)

1. 삭제할 노드를 찾음
2. 삭제할 노드의 successor 노드를 찾음
3. 삭제할 노드와 successor 노드의 값을 바꿈
4. successor 노드를 삭제
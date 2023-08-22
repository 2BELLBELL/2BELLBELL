import sys
input = sys.stdin.readline

# 전위 순회 함수
def preorder(num):
    if num == 0:
        return
    print(word[num], end='')
    preorder(word.index(C1[num]))
    preorder(word.index(C2[num]))

# 중위 순회 함수
def inorder(num):
    if num == 0:
        return
    inorder(word.index(C1[num]))
    print(word[num], end='')
    inorder(word.index(C2[num]))

# 후위 순회 함수
def postorder(num):
    if num == 0:
        return
    postorder(word.index(C1[num]))
    postorder(word.index(C2[num]))
    print(word[num], end='')

N = int(input())
word = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
C1 = ['0'] * 27
C2 = ['0'] * 27

# 트리 정보 입력
for i in range(1, N + 1):
    p, c1, c2 = input().split()
    if c1 != '.':
        C1[word.index(p)] = c1
    if c2 != '.':
        C2[word.index(p)] = c2

preorder(1)
print()
inorder(1)
print()
postorder(1)
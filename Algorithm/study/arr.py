from pprint import pprint as pp

m = 5
n = 5
arr = []

for i in range(n):
    row = [0] * m
    arr.append(row)
# pp(arr)

num_list = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

# # 1. 행 우선 순회
# for r in range(len(num_list)):
#     for c in range(len(num_list)):
#         print(f'{num_list[r][c]}', end=' ')  # 1 2 3 4 5 6 7 8 9

# # 2. 열 우선 순회
# for c in range(len(num_list)):
#     for r in range(len(num_list)):
#         print(f'{num_list[r][c]}')

# # 3. 역 - 행 우선 순회
# for i in range(len(num_list)):
#     for j in range(len(num_list)-1, -1, -1):
#         print(num_list[i][j])

# # 4. 역 - 열 우선 순회
# for j in range(len(num_list) -1, -1, -1):
#     for i in range(len(num_list)):
#         print(num_list[i][j], end=' ')
#     print()

# # 가장자리의 합
#
# def edge_sum(arr):
#     '''
#     2차원 리스트를 순회하면서
#     가장자리에 있는 원소들의 합을 구하는 함수
#     '''
#     edge_sum_result = 0
#     for i in range(len(arr)):
#         for j in range(len(arr[0])):
#             if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr) - 1:
#                 print(arr[i][j])
#                 edge_sum_result += arr[i][j]
#
#     return edge_sum_result
#
# result = edge_sum(num_list)
# print(result)

# 델타 탐색
# 문제에 제시된 제약 조건에 따라 탐색 순서는 달라질 수 있다.

#         # 상 하 좌 우
# d_row = [-1, 1, 0, 0]
# d_col = [0, 0, -1, 1]
#
#        # 좌상단    우상단   우하단   좌하단
# dxy = [(-1, -1), (-1, 1), (1, 1), (1, -1)]


# 주어진 2차원 리스트의 범위를 벗어나지 않게 제한 하는 행위가 필요

# 1. 벽을 넘는 경우, 아무것도 하지 않는다
# 2. 벽을 넘어가지 않는 경우에만 기능을 수행한다.
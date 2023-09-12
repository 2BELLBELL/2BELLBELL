import sys
input = sys.stdin.readline

S = input()
q = int(input())
# 누적합을 알파벳별로 채워넣을 2차원 배열
sum_arr = [[0] * 26 for _ in range(len(S) + 1)]

# 알파벳 별 배열에 열별로 채워넣기
for i in range(1, len(S) + 1):
    for j in range(26):
        if ord(S[i - 1])-97 == j:
            sum_arr[i][j] = sum_arr[i-1][j] + 1
        else:
            sum_arr[i][j] = sum_arr[i-1][j]

# 해당 알파벳의 r까지의 누적합 - l까지의 누적합 출력
for i in range(q):
    alphabet, l, r = input().split()
    print(sum_arr[int(r) + 1][ord(alphabet) - 97]-sum_arr[int(l)][ord(alphabet) - 97])
import sys
input = sys.stdin.readline

S = input()
q = int(input())
sum_arr = [[] for _ in range(26)]
for i in range(q):
    alphabet, l, r = input().split()
    # 해당 알파벳번째의 sum_arr 배열이 비어있다면 채우기
    if not sum_arr[ord(alphabet) - 97]:
        for j in range(len(S)):
            if S[j] == alphabet:
                sum_arr[ord(alphabet) - 97].append(j)
    cnt = 0
    for j in sum_arr[ord(alphabet) - 97]:
        if int(l) <= j <= int(r):
            cnt += 1

    print(cnt)
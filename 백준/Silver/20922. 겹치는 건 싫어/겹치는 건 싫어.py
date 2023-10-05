N, K = map(int, input().split())
arr = list(map(int, input().split()))
start = end = 0
dic = {}
max_len = 0
while end != N:
    # end를 전진하며 처음 등장하는 숫자면 딕셔너리에 넣는다
    if arr[end] not in dic:
        dic[arr[end]] = 1
    # 이미 딕셔너리에 있는 숫자라면
    elif arr[end] in dic:
        # 현재 등장 횟수가 K보다 적다면 1을 더한다
        if dic[arr[end]] < K:
            dic[arr[end]] += 1
        # 현대 등장 횟수가 K와 동일하다면 최대 길이를 갱신한다
        elif dic[arr[end]] == K:
            dic[arr[end]] += 1
            max_len = max(max_len, end - start)
            # 현재 K 를 초과한 숫자가 다시 K 이하가 될 때까지 start를 전진시킨다
            while True:
                dic[arr[start]] -= 1
                if dic[arr[start]] == K:
                    start += 1
                    break
                start += 1
    end += 1

max_len = max(max_len, end - start)
print(max_len)
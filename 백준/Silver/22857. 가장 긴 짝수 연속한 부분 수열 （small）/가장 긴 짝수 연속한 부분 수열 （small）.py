N, K = map(int, input().split())
S = list(map(int, input().split()))
start = end = 0
check = {
    'odd': 0,
    'even': 0
}
answer = 0
while end != N:
    # 짝수
    if S[end] % 2 == 0:
        check['even'] += 1
    # 홀수
    elif S[end] % 2 == 1:
        check['odd'] += 1

    # 홀수가 K를 넘은 경우
    if check['odd'] > K:
        # 최대 값 연속 짝수 부분 수열 갱신
        answer = max(answer, check['even'])
        # 홀수가 K개가 되도록 start 전진
        while check['odd'] != K:
            # 짝수
            if S[start] % 2 == 0:
                check['even'] -= 1
            # 홀수
            elif S[start] % 2 == 1:
                check['odd'] -= 1
            start += 1
    # end 전진
    end += 1
answer = max(answer, check['even'])
print(answer)
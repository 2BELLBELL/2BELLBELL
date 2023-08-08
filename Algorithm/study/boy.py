# 참고

# Skip table
# 1. 보이어무어 패턴 검색의 장점은 검색하는 패턴의 길이만큼 스킵할 수 있다는 점.
#    마지막 idx 를 제외할 것이다. -> pattern 의 마지막 인덱스를 검사했을 때,
#    일치하지 않는다면 len(pattern) 만큼 SKIP 할 것이다.
#    마지막에 나오는 Char 는 없는 거로 취급한다.

def pre_process(T):
    M = len(T)

    # 배열 대신 딕셔너리로 Skip table 구성
    skip_t = dict()
    # 기록되지 않은 문자는 get() 메서드의 default 값을 활용할 에정이다.
    for i in range(M - 1):
        skip_t[T[i]] = M - (1 + i)
    return skip_t

def boyer_moore(T, P):
    skip_t = pre_process(T)
    M = len(P)

    i = 0   # target idx
    while i <= len(T) - M:
        # print(i)
        # 뒤에서부터 탐색
        j = M - 1
        # 비교를 시작할 위치. (현재 위치 + M 번째 인덱스)
        k = i + M - 1

        # 탐색할 j idx 가 남아있고, target 과 pattern 이 같으면 1씩 줄여가면서 비교
        while j >= 0 and P[j] == T[k]:
            i -= 1
            j -= 1
        # 뒤에서부터 탐색을 하기 때문에, j가 -1값이 된다면 매칭이 성공했다는 듯
        if j == -1:
            position = i
            # print(position)
            return position

        # Skip 할 곳
        # i를 비교해서 탐색을 시작할 위치에 해당하는 문자 (T[i + M - 1])
        # skip_t에서 해당 문자를 찾아, 해당 문자의 Skip 값 만큼 스킵
        i += skip_t.get(T[i + M - 1], M)

    return -1


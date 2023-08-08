# Target : 검색 대상 // Pattern : 검색 패턴
target = "SSAFY 10th Let's go"
pattern = "go"

def bruteForce(patten, target):
    N = len(target)    # 검색 대상의 길이
    M = len(patten)    # 검색 패턴의 길이

    i = 0   # target 의 인덱스
    j = 0   # pattern 의 인덱스

    # 각 인덱스가 타겟과 패턴의 길이보다 작을동안 반복
    while j < M and i < N:
        # 패턴과 다른 곳을 발견 했을 때
        if target[i] != patten[j]:
            # j 만큼 온 상태에서 틀린 곳을 발견함.
            # 지금 위치 - j + 1 다음위치가 된다.
            i = i - j
            # -1 로 j 를 초기화 하는 이유, 패턴과 일치하는 문자열이 발견 됐을 때,
            # j + 1 을 해주기 때문
            j = - 1
        # 패턴과 같을 때
        i = i + 1
        j = j + 1

    if j == M:
        # 패턴 인덱스 j 가 패턴의 길이만큼 탐색 된 것 == 탐색 성공
        return i - M
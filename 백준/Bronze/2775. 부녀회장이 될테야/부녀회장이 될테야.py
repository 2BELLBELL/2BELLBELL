# Test Case의 수 입력받기
T = int(input())

# Test Case의 수만큼 k와 n 입력받기
for i in range(1, T + 1):
    k = int(input())
    n = int(input())
    A_list = []
    num_list = list(range(1, n + 1))
    j = [list((range(1, n + 1)))]

# 호의 갯수만큼 ho를 실행
    for ho in range(0, k):
# jj라는 빈리스트와 cnt라는 정수 생성
        jj = []
        cnt = 0
# 호의 갯수 만큼 kk를 동작 : 미리 만들어둔 j 리스트의 0번째 리스트에
        for kk in range(n):
            cnt = cnt + j[0][kk]
            jj.append(cnt)
        j.insert(0, jj)

    j = j[::-1]
    print(j[k][n - 1])